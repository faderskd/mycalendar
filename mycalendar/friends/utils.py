from django.contrib.auth import get_user_model
from django.db.models import Q


def search_users(string):
    """
    Search for user whose first name, last name
    or username starts with string
    """

    # Search when string has more than 4 characters.
    # It lets to avoid to many results returned.
    users = get_user_model().objects.none()
    if string and len(string) > 3:
        phrases = string.split()
        for phrase in phrases:
            users |= get_user_model().objects.filter(
                Q(username__istartswith=phrase) |
                Q(first_name__istartswith=phrase) |
                Q(last_name__istartswith=phrase)
            )
    return users
