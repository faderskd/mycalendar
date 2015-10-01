from django import template

from friends.models import Friendship

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_friendship_object(context, to_user):
    from_user = context['user']
    friendship = Friendship.objects.get(
        from_user=from_user,
        to_user=to_user
    )
    return friendship


@register.assignment_tag(takes_context=True)
def is_friend(context, other_user):
    user = context['user']
    return user.is_friend(other_user)


@register.assignment_tag(takes_context=True)
def invitation_sent_or_received(context, other_user):
    user = context['user']
    return user.invitation_sent_or_received(other_user)