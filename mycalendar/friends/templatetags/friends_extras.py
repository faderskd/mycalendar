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

