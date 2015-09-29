from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from friends.models import Friendship


class User(AbstractUser):
    photo = models.ImageField(
        _('photo'),
        null=True,
        blank=True,
        upload_to='users/photos'
    )
    # Recursive relation with intermediate model requires
    # 'symmetrical=False'.
    friends = models.ManyToManyField(
        'self',
        verbose_name=_('friends'),
        through=Friendship,
        symmetrical=False
    )

    def is_friend(self, user):
        return Friendship.are_friends(self, user)

    def add_friend(self, user):
        relationship, created = Friendship.objects.get_or_create(
            from_user=self,
            to_user=user
        )
        # If I am your friend, you are mine.
        # We have to preserve symmetric relationship
        Friendship.objects.get_or_create(
            from_user=user,
            to_user=self
        )
        return relationship

    def remove_friend(self, user):
        # Remove both direct and reverse relation.
        #TODO send notification to user about friendship deletion
        Friendship.objects.filter(
            Q(from_user=self, to_user=user) |
            Q(from_user=user, to_user=self)
        ).delete()

    def __str__(self):
        return self.username
