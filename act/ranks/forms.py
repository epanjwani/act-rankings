from django import forms
from .models import Player, ACT, Team, Race

class actForm(forms.ModelForm):
    class Meta:
        model = ACT
        fields = ['name', 't1player1', 't1player2', 't1character_1', 't1character_2','t2player1', 't2player2', 't2character_1', 't2character_2', 't3player1', 't3player2', 't3character_1', 't3character_2','t4player1', 't4player2', 't4character_1', 't4character_2']


class raceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'team1racer', 'points1', 'team2racer', 'points2', 'team3racer', 'points3', 'team4racer', 'points4']

