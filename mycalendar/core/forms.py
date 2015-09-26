from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username')}),
                                max_length=254)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
                             required=True, max_length=254)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Password')}), min_length=6)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder': _('Password (again)')}), min_length=6)

    class Meta:
        model = get_user_model()
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


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username')}),
                               max_length=254)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')}))


