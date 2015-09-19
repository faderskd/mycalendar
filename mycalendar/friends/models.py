from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel


class Friendship(TimeStampedModel):
    """
    Represents friendship between two people.
    """
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('from user'),
        related_name='sent_friendships'
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('to user'),
        related_name='received_friendships'
    )

    class Meta:
        verbose_name = _('Friendship')
        verbose_name_plural = _('Friendships')
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "From:{from_user} To:{to_user}".format(from_user=self.from_user, to_user=self.to_user)

    @classmethod
    def are_friends(cls, user1, user2):
        relation1 = cls.objects.filter(from_user=user1, to_user=user2).exists()
        relation2 = cls.objects.filter(from_user=user2, to_user=user1).exists()
        return relation1 and relation2


class FriendshipRequest(TimeStampedModel):
    """
    Represents friendship invitation from sender to receiver.
    """
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('sender'),
        related_name='sent_friendship_requests'
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('receiver'),
        related_name='received_friendships_requests'
    )
    viewed = models.BooleanField(
        _('viewed'),
        default=False
    )

    class Meta:
        verbose_name = _('FriendshipRequest')
        verbose_name_plural = _('FriendshipRequests')
        ordering = ('created',)

    def __str__(self):
        return "From:{sender} To:{receiver}".format(sender=self.sender, receiver=self.receiver)

    def accept(self):
        #TODO send notification to sender about acceptation
        Friendship.objects.create(from_user=self.sender, to_user=self.receiver)
        Friendship.objects.create(from_user=self.receiver, to_user=self.sender)
        self.delete()

    def reject(self):
        #TODO send notifiaction to sender about rejection
        self.delete()
