from django import forms
from .models import Player, ACT

class teamForm(forms.ModelForm):
    class Meta:
        model = ACT
        fields = ['team1', 'team2', 'team3', 'team4']
        