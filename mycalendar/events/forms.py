import itertools

from django import forms
from django.forms import widgets
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Event, EventCategory


class EventForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Event.objects.none(),
                                      widget=widgets.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        exclude = ('user', 'slug')
        # Adds class attributes for bootstrap styling.
        widgets = {
            'title': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start': forms.DateTimeInput(attrs={'class': 'datepicker form-control'}),
            'end': forms.DateTimeInput(attrs={'class': 'datepicker form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # Gets current user
        user = kwargs.pop('user')
        # Lists all user's event categories to be displayed on form.
        qs = user.event_categories.all()
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = qs

    def save(self, *args, **kwargs):
        instance = super(EventForm, self).save(commit=False)

        instance.slug = slugify(instance.title)

        # Checks slugfield max length
        max_length = Event._meta.get_field('slug').max_length
        # Cuts slug content to be proper size
        instance.slug = orig = slugify(instance.title)[:max_length]

        # Checks if slug (saved in orig temporary variable) exists already in database.
        # If exists adds "-number" to the end of slug, reserve uniqueness. Number is generated
        # as long as not exists in database. For example if slug "hello world" exists in database
        # and max slugfield length is 11 it will be replaced by hello wor-1
        for x in itertools.count(1):
            event_for_user_exists = Event.objects.filter(slug=instance.slug, user=instance.user). \
                exclude(id=self.instance.id).exists()
            if not event_for_user_exists:
                break
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()
        return instance


class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        exclude = ('user', 'slug')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(EventCategoryForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(EventCategoryForm, self).clean()
        name = self.cleaned_data.get('name')
        # If EventCategory object is edited (instance.id other than None) exlude this one and
        # check if another exists in database.
        any_other_category_exists = EventCategory.objects.filter(name=name, user=self.user). \
            exclude(id=self.instance.id).exists()
        # If EventCategory is create just check if another exists in database.
        any_category_exists = EventCategory.objects.filter(name=name, user=self.user).exists()

        # User editing category
        if self.instance.id and name and any_other_category_exists:
            raise ValidationError(_('Category already exists'))
        # User creating category
        elif not self.instance.id and name and any_category_exists:
            raise ValidationError(_('Category already exists'))

    def save(self, *args, **kwargs):
        instance = super(EventCategoryForm, self).save(commit=False)

        instance.slug = slugify(instance.name)

        # Checks slugfield max length
        max_length = Event._meta.get_field('slug').max_length
        # Cuts slug content to be proper size
        instance.slug = orig = slugify(instance.name)[:max_length]



        for x in itertools.count(1):
            if not EventCategory.objects.filter(slug=instance.slug, user=instance.user). \
                    exclude(id=self.instance.id).exists():
                break
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()
        return instance
