from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from users import models as users_models


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=254, label=_("Email"))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput, min_length=6, label=_("Password"))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput, min_length=6, label=_("Password (again)"))

    class Meta:
        model = users_models.User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(_('Passwords don"t match please type them again'))
        return cleaned_data

    def save(self, *args, **kwargs):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user





