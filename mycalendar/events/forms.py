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
        widgets = {
            'title': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start': forms.DateTimeInput(attrs={'class': 'datepicker form-control'}),
            'end': forms.DateTimeInput(attrs={'class': 'datepicker form-control'}),
            'category': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        qs = user.event_categories.all()
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = qs

    def save(self, commit=True):
        instance = super(EventForm, self).save(commit=False)

        instance.slug = slugify(instance.title)

        max_length = Event._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.title)[:max_length]

        for x in itertools.count(1):
            if not Event.objects.filter(slug=instance.slug, user=instance.user).exclude(id=self.instance.id).exists():
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
        name = self.cleaned_data.get('name')
        super(EventCategoryForm, self).clean()
        if self.instance.id and name and EventCategory.objects.filter(name=name, user=self.user).exclude(self.instance.id).exists():
            raise ValidationError(_('Category already exists'))
        elif name and EventCategory.objects.filter(name=name, user=self.user).exists():
            raise ValidationError(_('Category already exists'))

    def save(self, commit=True):
        instance = super(EventCategoryForm, self).save(commit=False)

        instance.slug = slugify(instance.name)

        max_length = Event._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.name)[:max_length]

        for x in itertools.count(1):
            if not EventCategory.objects.filter(slug=instance.slug, user=instance.user).exclude(id=self.instance.id).exists():
                break
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()
        return instance

