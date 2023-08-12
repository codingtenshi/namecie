from django import forms

class TeamForm(forms.Form):
    team_name = forms.CharField(max_length=100)
    team_description = forms.CharField(widget=forms.Textarea)
    year_founded = forms.ImageField()