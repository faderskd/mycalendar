from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError

import datetime
from colorful.fields import RGBColorField

from core.models import TimeStampedModel


class EventCategory(TimeStampedModel):
    name = models.CharField(
        _('name'),
        max_length=255
    )
    color = RGBColorField(
        _('color')
    )

    def __str__(self):
        return self.name


class Event(TimeStampedModel):
    title = models.CharField(
        _('title'),
        max_length=255
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

    def clean(self):
        if self.start and self.end and self.start - self.end > datetime.timedelta(0):
            raise ValidationError(_("End date mustn't be before start date"))

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('events:edit', args=[str(self.id)])

    def __str__(self):
        return self.title
