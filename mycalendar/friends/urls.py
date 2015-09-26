from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.FriendsListView.as_view(), name='friends-list'),
    url(r'^search-list-json/$', views.FriendsJSONSearchListView.as_view(), name='search-friends-list-json'),
    url(r'^create_friendship_request/$', views.FriendshipRequestCreateView.as_view(), name='create-friendship-request'),
]
