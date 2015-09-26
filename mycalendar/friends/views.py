from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from braces.views import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Friendship, FriendshipRequest
from .utils import search_users
from .permissions import IsRequestAjax
from users.serializers import UserSerializer


class FriendsJSONSearchListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        username = self.request.GET.get('username')
        search_results = search_users(username)
        return search_results


class FriendsListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = 'friends_list'
    template_name = 'friends/friends_list.html'

    def get_queryset(self):
        return self.request.user.friends.all()


class FriendshipRequestCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = FriendshipRequest
    fields = ('receiver',)
    template_name = 'friends/friendship_request_create_form.html'
    success_url = reverse_lazy('friends:create-friendship-request')
    success_message = _('Invitation sent')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FriendshipRequestCreateView, self).form_valid(form)