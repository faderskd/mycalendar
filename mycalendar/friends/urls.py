from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.FriendsListView.as_view(), name='list'),
    url(r'^search-list-json/$', views.FriendsJSONSearchListView.as_view(), name='search-json'),
    url(r'^(?P<username>\w+)/details/$', views.FriendshipRequestCreateView.as_view(), name='invite'),
    url(r'^invite/$', views.FriendshipRequestCreateView.as_view(), name='invite'),
]
