from django.views import generic

from rest_framework.generics import ListAPIView

from .models import Event
from .serializers import EventSerializer


class EventJSONListView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return self.request.user.events.all()


class EventCalendarView(generic.ListView):
    template_name = 'events/event_calendar.html'
    model = Event
    context_object_name = 'event_list'

    def get_queryset(self):
        return self.request.user.events.all()

