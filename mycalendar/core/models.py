from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract model to be inherited by other models for storing repetitive dates
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
