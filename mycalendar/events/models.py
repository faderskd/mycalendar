import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from colorful.fields import RGBColorField

from core.models import TimeStampedModel


class EventCategory(TimeStampedModel):
    """
    Category to enable grouping users events
    """
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    color = RGBColorField(
        _('color')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='event_categories'
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = _('EventCategory')
        verbose_name_plural = _('EventCategories')
        unique_together = ['name', 'user']

    def get_absolute_url(self):
        return reverse('events:categories:edit-category', kwargs={'username': self.user.username, 'slug': self.slug})

    def __str__(self):
        return self.name


class Event(TimeStampedModel):
    """
    Event for particular user
    """
    title = models.CharField(
        _('title'),
        max_length=255,
    )
    description = models.TextField(
        _('desription'),
        blank=True
    )
    start = models.DateTimeField(
        _('start time')
    )
    end = models.DateTimeField(
        _('end time')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name= _('user'),
        related_name='events'
    )
    category = models.ForeignKey(
        'EventCategory',
        verbose_name= _('category'),
        related_name='events'
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        unique_together = ['user', 'slug']

    def clean(self):
        if self.start and self.end and self.start - self.end > datetime.timedelta(0):
            raise ValidationError(_("End date mustn't be before start date"))

    def get_absolute_url(self):
        return reverse('events:edit-event', kwargs={'username': self.user.username, 'slug': self.slug})

    def __str__(self):
        return self.title
