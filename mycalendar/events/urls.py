from django.conf.urls import url, include

from . import views

event_categories_urlpatterns = [
    url(r'^$', views.EventCategoryListView.as_view(), name='categories-list'),
    url(r'^create/$', views.EventCategoryCreateView.as_view(), name='create-category'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/edit/$', views.EventCategoryUpdateView.as_view(), name='edit-category'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/delete/$', views.EventCategoryDeleteView.as_view(), name='delete-category'),
]

urlpatterns = [
    url(r'^$', views.EventCalendarView.as_view(), name='events-calendar'),
    url(r'^create/$', views.EventCreateView.as_view(), name='create-event'),
    url(r'^list-json/$', views.EventJSONListView.as_view(), name='events-list-json'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/edit/$', views.EventUpdateView.as_view(), name='edit-event'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/delete/$', views.EventDeleteView.as_view(), name='delete-event'),
    url(r'^categories/', include(event_categories_urlpatterns, namespace='categories')),
]
