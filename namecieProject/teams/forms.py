from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator

class TeamForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nazwa')
    team_description = forms.CharField(widget=forms.Textarea, label='Opis grupy')
    year_founded = forms.IntegerField(label="Rok założenia")
   