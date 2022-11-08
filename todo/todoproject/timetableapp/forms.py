from django import forms
from .models import Timetable
class TodoForms(forms.ModelForm):
    class Meta:
        model=Timetable
        fields=['day','task','date',]