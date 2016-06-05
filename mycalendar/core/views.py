from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.views import login as auth_login, logout as auth_logout
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from .forms import RegistrationForm, LoginForm
from users import models as users_models


def login(request, **kwargs):
    """
    If user is signed in redirects to main page, if not returns base django authentication view
    """
    print(request.POST)
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    return auth_login(request, authentication_form=LoginForm, **kwargs)


def logout(request):
    """
    Logouts user and redirects to login page
    """
    return auth_logout(request, next_page=settings.LOGIN_URL)


class RegisterView(SuccessMessageMixin, CreateView):
    model = users_models.User
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = _('Your account was created, now you can sing in')
