from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from core.views import login, logout

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='login', permanent=True)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^events/', include('events.urls', namespace='events')),
]

