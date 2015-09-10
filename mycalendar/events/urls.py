from django.conf.urls import url, include

from .views import (EventCalendarView, EventJSONListView, EventCreateView, EventUpdateView, EventDeleteView,
                    EventCategoryListView, EventCategoryCreateView, EventCategoryUpdateView, EventCategoryDeleteView)

event_categories_urlpatterns = [
    url(r'^$', EventCategoryListView.as_view(), name='categories-list'),
    url(r'^create/$', EventCategoryCreateView.as_view(), name='create-category'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/edit/$', EventCategoryUpdateView.as_view(), name='edit-category'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/delete/$', EventCategoryDeleteView.as_view(), name='delete-category'),
]

urlpatterns = [
    url(r'^$', EventCalendarView.as_view(), name='events-calendar'),
    url(r'^list-json/$', EventJSONListView.as_view(), name='list-json'),
    url(r'^create/$', EventCreateView.as_view(), name='create-event'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/edit/$', EventUpdateView.as_view(), name='edit-event'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/delete/$', EventDeleteView.as_view(), name='delete-event'),
    url(r'^categories/', include(event_categories_urlpatterns, namespace='categories')),
]
