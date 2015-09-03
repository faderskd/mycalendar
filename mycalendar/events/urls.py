from django.conf.urls import url

from .views import EventCalendarView, EventJSONListView, EventCreateView, EventUpdateView

urlpatterns = [
    url(r'^$', EventCalendarView.as_view(), name='events-calendar'),
    url(r'^list-json/$', EventJSONListView.as_view(), name='list-json'),
    url(r'^create/$', EventCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', EventUpdateView.as_view(), name='edit')
]
