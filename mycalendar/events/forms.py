from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user', )
        widgets = {
            'title': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start': forms.DateTimeInput(attrs={'class': 'datepicker form-control'}),
            'end': forms.DateTimeInput(attrs={'class': 'datepicker form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
