from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model

from braces.views import LoginRequiredMixin

from .models import Friendship, FriendshipRequest


class FriendsListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = 'friendship_list'
    template_name = 'friends/friends_list.html'

    def get_queryset(self):
        return self.request.user.friends.all()
