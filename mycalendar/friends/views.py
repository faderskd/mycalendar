from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Friendship, Invitation
from .utils import search_users
from .permissions import IsRequestAjax
from users.serializers import UserSerializer


class FriendJSONSearchListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsRequestAjax)

    def get_queryset(self):
        qs = self.request.GET.get('qs')
        search_results = search_users(qs)
        return search_results


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
        obj = get_object_or_404(get_user_model(), username=username)
        return obj


class InvitationCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Invitation
    fields = ('receiver',)
    template_name = 'friends/invitation_form.html'
    success_url = reverse_lazy('friends:list')
    success_message = _('Invitation sent')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InvitationCreateView, self).form_valid(form)


class InvitationList(LoginRequiredMixin, generic.ListView):
    template_name = 'friends/invitation_list.html'
    context_object_name = 'invitation_list'

    def get_queryset(self):
        qs = self.request.GET.get('qs')
        if qs == 'sent':
            invitations = Invitation.objects.filter(
                sender=self.request.user
            )
        else:
            invitations = Invitation.objects.filter(
                receiver=self.request.user
            )
        return invitations
