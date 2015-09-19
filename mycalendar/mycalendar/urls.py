from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from core.views import login, logout, RegisterView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='login', permanent=True)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^friends/', include('friends.urls', namespace='friends')),
]
