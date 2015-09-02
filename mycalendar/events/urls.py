from django.conf.urls import url

from .views import EventCalendarView, EventJSONListView

urlpatterns = [
    url(r'^$', EventCalendarView.as_view(), name='events-calendar'),
    url(r'^list-json/$', EventJSONListView.as_view(), name='list-json')
]
