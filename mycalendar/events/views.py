from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

import datetime
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from braces.views import LoginRequiredMixin

from .models import Event
from .serializers import EventSerializer


class EventJSONListView(ListAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        start = self.request.GET.get('start', '')
        end = self.request.GET.get('end', '')
        if self._dates_are_valid(start, end):
            return self.request.user.events.filter(start__range=[start, end])
        return self.request.user.events.all()

    def _dates_are_valid(self, start, end):
        try:
            datetime.datetime.strptime(start, '%Y-%m-%d')
            datetime.datetime.strptime(end, '%Y-%m-%d')
        except ValueError:
            return False
        return True


class EventCalendarView(LoginRequiredMixin, generic.ListView):
    template_name = 'events/events_calendar.html'
    model = Event
    context_object_name = 'event_list'

    def get_queryset(self):
        return self.request.user.events.all()


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Event
    fields = ['title', 'description', 'start', 'end', 'category']
    success_message = _('Event created')
    success_url = reverse_lazy('events:create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start', 'end', 'category']
    success_message = _('Event updated')
    success_url = reverse_lazy('events:update')