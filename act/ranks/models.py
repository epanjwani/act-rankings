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
        ("Brian Volk", "BV")
    )
    name = models.CharField(max_length=50, choices=PLAYER_CHOICES)
    elo = models.IntegerField()
    elo_change = models.IntegerField(default=0)
    acts_ran = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    accum_competitor_elo = models.IntegerField(default=0)
    LEAGUE_CHOICES = (
        ("A-League", "A-League"),
        ("B-League", "B-League"),
        ("C-League", "C-League"),
        ("N/A", "N/A"),
    )
    league = models.CharField(max_length=50, choices=LEAGUE_CHOICES, null=True)
    def __str__(self):
        return self.name

class PlayerEntry(models.Model):
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
        ("Brian Volk", "BV")
    )
    name = models.CharField(max_length=50, choices=PLAYER_CHOICES)
    #races = models.ManyToManyField(Race)
    points = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

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
    team1racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t1entry")
    points1 = models.IntegerField()
    team2racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t2entry")
    points2 = models.IntegerField()
    team3racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t3entry")
    points3 = models.IntegerField()
    team4racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t4entry")
    points4 = models.IntegerField()
    def __str__(self):
        return self.name

class Team(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="p1")
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="p2")
    player1entry = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="p1entry")
    player2entry = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="p2entry")
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

class ACT(models.Model):
    CHARACTER_CHOICES = (
        ("Baby", "Baby"),
        ("Toad", "Toad"),
        ("Koopa", "Koopa"),
        ("Bowser Jr.", "Bowser Jr."),
        ("Diddy Kong", "Diddy Kong"),
        ("Medium character", "Medium character"),
        ("Big character", "Big character")
    )
    name = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(auto_now=True)
    t1player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t1p1")
    t1player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t1p2")
    t1character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)
    t1character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)
    t2player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t2p1")
    t2player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t2p2")
    t2character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)
    t2character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)
    t3player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t3p1")
    t3player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t3p2")
    t3character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)
    t3character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)
    t4player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t4p1")
    t4player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t4p2")
    t4character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)
    t4character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=False)

    def __str__(self):
        return self.name






