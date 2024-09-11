from django.forms import ModelForm
from django import forms
from .models import Pomodoro


class PomodoroForm(ModelForm):
    start_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )
    end_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )

    # widget=forms.DateTimeField(attrs={"type": "date"})
    class Meta:
        model = Pomodoro
        fields = ["start_date", "end_date", "finished"]
