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
        ("Brian Volk", "BV"),
        ("Nitan Shalon", "NSh"),
        ("Mat Zlotnick", "MZ"),
        ("Gavin Morse" , "GM"),
    )
    name = models.CharField(max_length=50, choices=PLAYER_CHOICES)
    elo = models.IntegerField(null=True)
    elo_change = models.IntegerField(default=0)
    elo_change1 = models.IntegerField(default=0)
    elo_change2 = models.IntegerField(default=0)
    elo_change3 = models.IntegerField(default=0)
    elo_change4 = models.IntegerField(default=0)
    elo_change5 = models.IntegerField(default=0)
    acts_ran = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    accum_competitor_elo = models.IntegerField(default=0)
    #accum_teammate_elo = models.IntegerField(default=0)
    LEAGUE_CHOICES = (
        ("A-League", "A-League"),
        ("C-League", "C-League"),
        ("N/A", "N/A"),
    )
    league = models.CharField(max_length=50, choices=LEAGUE_CHOICES, null=True)
    def __str__(self):
        return self.name

class ACT(models.Model):
    act_id = models.AutoField(primary_key=True)
    t1player1 = models.ForeignKey(Player)
    t1player2 = models.ForeignKey(Player)
    t2player1 = models.ForeignKey(Player)
    t2player2 = models.ForeignKey(Player)
    t3player1 = models.ForeignKey(Player)
    t3player2 = models.ForeignKey(Player)
    t4player1 = models.ForeignKey(Player)
    t4player2 = models.ForeignKey(Player)
    CHARACTER_CHOICES = (
        ("B", "B"),
        ("T", "T"),
        ("K", "K"),
        ("BJ", "BJ"),
        ("DK", "DK"),
        ("Medium character", "Medium character"),
        ("Big character", "Big character"),
        ("Other", "Other")
    )
    t1character1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t1character2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t2character1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t2character2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t3character1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t3character2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t4character1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t4character2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t1player1_scores = models.CharField(max_length=75, null=True)
    t1player2_scores = models.CharField(max_length=75, null=True)
    t2player1_scores = models.CharField(max_length=75, null=True)
    t2player2_scores = models.CharField(max_length=75, null=True)
    t3player1_scores = models.CharField(max_length=75, null=True)
    t3player2_scores = models.CharField(max_length=75, null=True)
    t1player1_scores = models.CharField(max_length=75, null=True)
    t4player2_scores = models.CharField(max_length=75, null=True)
    t1player1_elo_before = models.IntegerField(default=0)
    t1player2_elo_before = models.IntegerField(default=0)
    t2player1_elo_before = models.IntegerField(default=0)
    t2player2_elo_before = models.IntegerField(default=0)
    t3player1_elo_before = models.IntegerField(default=0)
    t3player2_elo_before = models.IntegerField(default=0)
    t4player1_elo_before = models.IntegerField(default=0)
    t4player2_elo_before = models.IntegerField(default=0)
    t1player1_elo_after = models.IntegerField(default=0)
    t1player2_elo_after = models.IntegerField(default=0)
    t2player1_elo_after = models.IntegerField(default=0)
    t2player2_elo_after = models.IntegerField(default=0)
    t3player1_elo_after = models.IntegerField(default=0)
    t3player2_elo_after = models.IntegerField(default=0)
    t4player1_elo_after = models.IntegerField(default=0)
    t4player2_elo_after = models.IntegerField(default=0)
    LEAGUE_CHOICES = (
        ("A-League", "A-League"),
        ("C-League", "C-League"),
        ("N/A", "N/A"),
    )
    league = models.CharField(max_length=50, choices=LEAGUE_CHOICES, null=True)

"""

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
    team1racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t1entry", null=True)
    points1 = models.IntegerField(null=True)
    team2racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t2entry", null=True)
    points2 = models.IntegerField(null=True)
    team3racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t3entry", null=True)
    points3 = models.IntegerField(null=True)
    team4racer = models.ForeignKey(PlayerEntry, on_delete=models.CASCADE, related_name="t4entry" , null=True)
    points4 = models.IntegerField(null=True)
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
    """




