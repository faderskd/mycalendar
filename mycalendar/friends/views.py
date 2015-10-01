from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.http import HttpResponseForbidden

from braces.views import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Invitation
from .utils import search_users
from .permissions import IsRequestAjax
from users.serializers import UserSerializer


class FriendJSONSearchListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = self.request.GET.get('qs')
        search_results = search_users(qs)
        return search_results

    model = get_user_model()
    context_object_name = 'friend_list'
    template_name = 'friends/friend_list.html'


class FriendListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = 'friend_list'
    template_name = 'friends/friend_list.html'

    def get_queryset(self):
        return self.request.user.friends.all()


class FriendDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = 'friends/friend_details.html'
    context_object_name = 'object'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        obj = get_object_or_404(
            get_user_model(),
            username=username
        )
        return obj


class InvitationListView(LoginRequiredMixin, generic.ListView):
    template_name = 'friends/invitation_list.html'
    context_object_name = 'invitation_list'

    def get(self, request, *args, **kwargs):
        status = self.request.GET.get('status')
        if status not in ['sent', 'received']:
            return redirect(reverse_lazy('friends:invitations:list') + '?status=received')
        return super(InvitationListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        status = self.request.GET.get('status')
        if status == 'received':
            invitations = Invitation.objects.filter(
                receiver=self.request.user
            )
        else:
            invitations = Invitation.objects.filter(
                sender=self.request.user
            )
        return invitations


class InvitationCreateView(LoginRequiredMixin, generic.View):
    def post(self, request, *args, **kwargs):
        username = self.kwargs.get('username')
        user = get_object_or_404(get_user_model(), username=username)
        logged_user = self.request.user
        # Deny sent invitation if was sent to user or received from user.
        if logged_user.invitation_sent_or_received(user) or logged_user == user:
            return HttpResponseForbidden()
        logged_user.send_invitation(user)
        messages.success(request, _('Invitation to user {user} sent').format(user=user))
        return redirect(reverse_lazy('friends:details', kwargs={'username': user.username}))


class InvitationAcceptView(LoginRequiredMixin, SingleObjectMixin, generic.View):
    def post(self, request, *args, **kwargs):
        invitation = self.get_object()
        invitation.accept()
        messages.success(request, _('Invitation from user {user} accepted'.format(user=invitation.sender)))
        return redirect(reverse_lazy('friends:list'))

    def get_object(self, queryset=None):
        sender = self.kwargs.get('username')
        obj = get_object_or_404(
            Invitation,
            sender__username=sender,
            receiver=self.request.user
        )
        return obj


class InvitationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Invitation
    template_name = 'friends/invitation_confirm_delete.html'
    success_url = reverse_lazy('friends:invitations:list')

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        obj = get_object_or_404(
            Invitation,
            Q(sender=self.request.user, receiver__username=username) |
            Q(sender__username=username, receiver=self.request.user)
        )
        return obj
