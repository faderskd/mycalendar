from django.conf.urls import url, include

from . import views

invitations_patterns = [
    url(r'^$', views.InvitationList.as_view(), name='list'),
    url(r'^create/$', views.InvitationCreateView.as_view(), name='create'),
    url(r'^(?P<username>\w+)/accept/$', views.InvitationAcceptView.as_view(), name='accept'),
]

urlpatterns = [
    url(r'^$', views.FriendListView.as_view(), name='list'),
    url(r'^search-list-json/$', views.FriendJSONSearchListView.as_view(), name='search-json'),
    url(r'^(?P<username>\w+)/details/$', views.FriendDetailView.as_view(), name='details'),
    url(r'^invitations/', include(invitations_patterns, namespace='invitations'))
]
