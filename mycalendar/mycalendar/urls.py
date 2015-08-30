from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='login', permanent=True)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout')
]
