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
        return "From:{from_user} To:{to_user}".format(
            from_user=self.from_user,
            to_user=self.to_user
        )

    @classmethod
    def are_friends(cls, user1, user2):
        """
        Check if friendship from user1 to user2 or from
        user2 to user1 exists
        """
        relation1_exists = cls.objects.filter(
            from_user=user1,
            to_user=user2
        ).exists()
        relation2_exists = cls.objects.filter(
            from_user=user2,
            to_user=user1
        ).exists()
        return relation1_exists and relation2_exists


class Invitation(TimeStampedModel):
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

    class Meta:
        verbose_name = _('Invitation')
        verbose_name_plural = _('Invitations')
        ordering = ('created',)

    def __str__(self):
        return "From:{sender} To:{receiver}".format(
            sender=self.sender,
            receiver=self.receiver
        )

    def accept(self):
        #TODO send notification to sender about acceptation
        self.receiver.add_friend(self.sender)
        self.delete()

    def reject(self):
        #TODO send notifiaction to sender about rejection
        self.delete()

    @classmethod
    def invitation_exists(cls, user1, user2):
        """
        Check if invitation from user1 to user2 or from
        user2 to user1 exists
        """
        cond1 = Invitation.objects.filter(
            sender=user1,
            receiver=user2
        ).exists()
        cond2 = Invitation.objects.filter(
            sender=user2,
            receiver=user1
        ).exists()
        return cond1 or cond2