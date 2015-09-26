from django.contrib.auth import get_user_model
from django.db.models import Q


def search_users(username):
    """
    Search for user with given username
    """

    # Search when username has more than 4 characters.
    # # It lets to avoid to many results returned.
    # phrases = username.split()
    # if len(phrases) == 1:
    #     if username and len(username) > 3:
    #         users = get_user_model().objects.filter(
    #             Q(username__istartswith=username) |
    #             Q(first_name__istartswith=username) |
    #             Q(last_name__istartswith=username)
    #         )
    #         return users
    #     return get_user_model().objects.none()
