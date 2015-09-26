from django.conf.urls import url, include

from . import views

event_categories_urlpatterns = [
    url(r'^$', views.EventCategoryListView.as_view(), name='list'),
    url(r'^create/$', views.EventCategoryCreateView.as_view(), name='create'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/edit/$', views.EventCategoryUpdateView.as_view(), name='edit'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/delete/$', views.EventCategoryDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    url(r'^$', views.EventCalendarView.as_view(), name='calendar'),
    url(r'^create/$', views.EventCreateView.as_view(), name='create'),
    url(r'^list-json/$', views.EventJSONListView.as_view(), name='list-json'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/edit/$', views.EventUpdateView.as_view(), name='edit'),
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)/delete/$', views.EventDeleteView.as_view(), name='delete'),
    url(r'^categories/', include(event_categories_urlpatterns, namespace='categories')),
]
