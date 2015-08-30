from django.views import generic
from events.models import Event, EventCategory


class EventCalendarView(generic.ListView):
    template_name = 'events/event_calendar.html'
    model = Event