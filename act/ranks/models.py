from django.db import models

class Player(models.Model):
    PLAYER_CHOICES = (
        ("Eashan Panjwani", "EP"),
        ("Zach Bell", "ZB"),
        ("Benner Mullin", "BM"),
        ("Jackson Brodwolf", "JB"),
        ("Matt Halper", "MH"),
        ("Alex Hazel", "AH"),
        ("Harris Klein", "HK"),
        ("Kohl Terry", "KT"),
        ("Alex Mellas", "AM"),
        ("Noah Paige", "NP"),
        ("Julian Ricci", "JR"),
        ("Robbie Kramer", "RK"),
        ("Ethan Roberts", "ER"),
        ("Henry Rogers", "HR"),
        ("Ryan Simon", "RS"),
        ("Peter Netch", "PN"),
        ("Andrew Schanny", "AS"),
        ("Avery Friedman", "AF"),
        ("Josh Greenfield", "JG"),
        ("Will Spartin", "WS"),
        ("Will Goldberg", "WG"),
        ("Brady Sheaffer", "BS"),
        ("Aman Patil", "AP"),
        ("Zach Stern", "ZS"),
        ("Josh Josef", "JJ"),
        ("Nico Simon", "NS"),
        ("Sam Schoepke", "SS"),
        ("James Berthoud", "JBe"),
        ("Jonathan Nurko", "JN"),
        ("Spencer Gladstone", "SG"),
        ("Kion Noori", "KN"),
        ("Max Marchetto", "MM"),
        ("Chuck Leonetti", "CL"),
        ("Matt Flower", "MF"),
        ("Connor Caz", "CC"),
        ("Caleb Hughes", "CH"),
        ("Lukas Steinbock", "LS"),
        ("Brian Volk", "BS")
    )
    name = models.CharField(max_length=50, choices=PLAYER_CHOICES)
    elo_rating = models.IntegerField()
    races = models.ManyToManyField(Race)
    points = models.IntegerField()


class Team(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE)
    CHARACTER_CHOICES = (
        ("Baby", "Baby"),
        ("Toad", "Toad"),
        ("Koopa", "Koopa"),
        ("Bowser Jr.", "Bowser Jr."),
        ("Diddy Kong", "Diddy Kong"),
        ("Medium character", "Medium character"),
        ("Big character", "Big character")
    )
    character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES)
    character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES)
    avg_elo = models.IntegerField()

class Race(models.Model):
    RACE_CHOICES = (
        ("Luigi Circuit", "Luigi Circuit"),
        ("Peach Beach", "Peach Beach"),
        ("Baby Park", "Baby Park"),
        ("Dry Dry Desert", "Dry Dry Desert"),
        ("Mushroom Bridge", "Mushroom Bridge"),
        ("Mario Circuit", "Mario Circuit"),
        ("Daisy Cruiser", "Daisy Cruiser"),
        ("Waluigi Stadium", "Waluigi Stadium"),
        ("Sherbet Land", "Sherbet Land"),
        ("Mushroom City", "Mushroom City"),
        ("Yoshi Circuit", "Yoshi Circuit"),
        ("DK Mountain", "DK Mountain"),
        ("Wario Colloseum", "Wario Colloseum"),
        ("Dino Dino Jungle", "Dino Dino Jungle"),
        ("Bowser Castle", "Bowser Castle"),
        ("Rainbow Road", "Rainbow Road")
    )
    name = models.CharField(max_length=50, choices=RACE_CHOICES)

class ACT(models.Model):
    date = models.DateTimeField(auto_now=True)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team3 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team4 = models.ForeignKey(Team, on_delete=models.CASCADE)







