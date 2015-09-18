import datetime

from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from braces.views import LoginRequiredMixin, UserPassesTestMixin

from .models import Event, EventCategory
from .serializers import EventSerializer
from .forms import EventForm, EventCategoryForm


class EventJSONListView(ListAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        start = self.request.GET.get('start', '')
        end = self.request.GET.get('end', '')
        if self._dates_are_valid(start, end):
            return self.request.user.events.filter(start__range=[start, end])
        return self.request.user.events.all()

    @staticmethod
    def _dates_are_valid(start, end):
        try:
            datetime.datetime.strptime(start, '%Y-%m-%d')
            datetime.datetime.strptime(end, '%Y-%m-%d')
        except ValueError:
            return False
        return True


class EventCalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'events/events_calendar.html'

    def get_queryset(self):
        return self.request.user.events.all()


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_create_form.html'
    success_url = reverse_lazy('events:create-event')
    success_message = _('Event created')

    def get_form_kwargs(self):
        kwargs = super(EventCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_edit_form.html'
    success_message = _('Event updated')

    def test_func(self, user):
        event = self.get_object()
        return event.user == user

    def get_object(self, queryset=None):
        super(EventUpdateView, self).get_object()
        username = self.kwargs.get('username')
        slug = self.kwargs.get('slug')
        return get_object_or_404(Event, user__username=username, slug=slug)

    def get_form_kwargs(self):
        kwargs = super(EventUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('events:events-calendar')
    context_object_name = 'event'

    def test_func(self, user):
        event = self.get_object()
        return event.user == user

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        slug = self.kwargs.get('slug')
        return get_object_or_404(Event, user__username=username, slug=slug)


class EventCategoryListView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    model = EventCategory
    context_object_name = 'event_category_list'
    template_name = 'events/event_category_list.html'

    def get_queryset(self):
        return self.request.user.event_categories.all()


class EventCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = EventCategory
    form_class = EventCategoryForm
    template_name = 'events/event_category_create_form.html'
    success_url = reverse_lazy('events:categories:create-category')
    success_message = _('Event category created')

    def get_form_kwargs(self):
        kwargs = super(EventCategoryCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCategoryCreateView, self).form_valid(form)


class EventCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = EventCategory
    form_class = EventCategoryForm
    template_name = 'events/event_category_edit_form.html'
    success_message = _('Event category updated')

    def test_func(self, user):
        event_category = self.get_object()
        return event_category.user == user

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        slug = self.kwargs.get('slug')
        return get_object_or_404(EventCategory, user__username=username, slug=slug)

    def get_form_kwargs(self):
        kwargs = super(EventCategoryUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class EventCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = EventCategory
    template_name = 'events/event_category_confirm_delete.html'
    success_url = reverse_lazy('events:categories:categories-list')
    context_object_name = 'event_category'

    def test_func(self, user):
        event_category = self.get_object()
        return event_category.user == user

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        slug = self.kwargs.get('slug')
        return get_object_or_404(EventCategory, user__username=username, slug=slug)
