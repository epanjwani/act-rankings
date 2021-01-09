from django.db import models

# Create your models here.

class Player(models.Model):
    PLAYER_CHOICES = (
        ("Eashan Panjwani", "EP"),
        ("Zach Bell", "ZB"),
        ("Noah Paige", "NP"),
    )
    name = models.CharField(max_length=50, choices=PLAYER_CHOICES)
    elo_rating = models.IntegerField()

class Team(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE)
    num_points = models.IntegerField()
    CHARACTER_CHOICES = (
        ("Baby Mario", "Baby Mario"),
        ("Baby Luigi", "Baby Luigi")
        ("Toad", "Toad"),
        ("Toadette", "Toadette"),
        ("Baby Koopa", "Baby Koopa"),
        ("Diddy Kong", "Diddy Kong"),
        #add rest of characters

    )
    character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES)
    character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES)

#class Race(models.Model):

class ACT(models.Model):
    date = models.DateTimeField(auto_now=True)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team3 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team4 = models.ForeignKey(Team, on_delete=models.CASCADE)






