from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EventCalendarView.as_view(), name='events-calendar'),
]
