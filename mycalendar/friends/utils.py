from django.contrib.auth import get_user_model
from django.db.models import Q


def search_users(username):
    """
    Search for user with given username
    """

    # Search when username has more than 4 characters.
    # It lets to avoid to many results returned.
    users = get_user_model().objects.none()
    if username and len(username) > 3:
        phrases = username.split()
        for phrase in phrases:
            users |= get_user_model().objects.filter(
                Q(username__istartswith=phrase) |
                Q(first_name__istartswith=phrase) |
                Q(last_name__istartswith=phrase)
            )
    return users
