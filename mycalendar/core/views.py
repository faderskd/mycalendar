from django.shortcuts import redirect
from django.contrib.auth.views import login as auth_login, logout as auth_logout
from django.conf import settings


def login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    return auth_login(request, **kwargs)


def logout(request):
    return auth_logout(request, next_page=settings.LOGIN_URL)
