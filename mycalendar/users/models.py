from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from friends.models import Friendship


class User(AbstractUser):
    photo = models.ImageField(
        _('photo'),
        null=True,
        upload_to='users/photos'
    )
    friends = models.ManyToManyField(
        'self',
        verbose_name=_('friends'),
        through=Friendship,
        symmetrical=False
    )

    def __str__(self):
        return self.username
