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
    elo = models.IntegerField(null=True)
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
    name = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now=True)
    t1player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t1p1", null=True)
    t1player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t1p2", null=True)
    t1character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t1character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t2player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t2p1", null=True)
    t2player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t2p2", null=True)
    t2character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t2character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t3player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t3p1", null=True)
    t3player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t3p2", null=True)
    t3character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t3character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t4player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t4p1", null=True)
    t4player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="t4p2", null=True)
    t4character_1 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
    t4character_2 = models.CharField(max_length=50, choices=CHARACTER_CHOICES, null=True)
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
    oneteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    onepoints1 = models.IntegerField(null=True)
    oneteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    onepoints2 = models.IntegerField(null=True)
    oneteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    onepoints3 = models.IntegerField(null=True)
    oneteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    onepoints4 = models.IntegerField(null=True)
    twoteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twopoints1 = models.IntegerField(null=True)
    twoteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twopoints2 = models.IntegerField(null=True)
    twoteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twopoints3 = models.IntegerField(null=True)
    twoteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twopoints4 = models.IntegerField(null=True)
    threeteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    threepoints1 = models.IntegerField(null=True)
    threeteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    threepoints2 = models.IntegerField(null=True)
    threeteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    threepoints3 = models.IntegerField(null=True)
    threeteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    threepoints4 = models.IntegerField(null=True)
    fourteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourpoints1 = models.IntegerField(null=True)
    fourteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourpoints2 = models.IntegerField(null=True)
    fourteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourpoints3 = models.IntegerField(null=True)
    fourteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourpoints4 = models.IntegerField(null=True)
    fiveteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fivepoints1 = models.IntegerField(null=True)
    fiveteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fivepoints2 = models.IntegerField(null=True)
    fiveteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fivepoints3 = models.IntegerField(null=True)
    fiveteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fivepoints4 = models.IntegerField(null=True)
    sixteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixpoints1 = models.IntegerField(null=True)
    sixteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixpoints2 = models.IntegerField(null=True)
    sixteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixpoints3 = models.IntegerField(null=True)
    sixteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixpoints4 = models.IntegerField(null=True)
    seventeam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sevenpoints1 = models.IntegerField(null=True)
    seventeam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sevenpoints2 = models.IntegerField(null=True)
    seventeam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sevenpoints3 = models.IntegerField(null=True)
    seventeam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sevenpoints4 = models.IntegerField(null=True)
    eightteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    eightpoints1 = models.IntegerField(null=True)
    eightteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    eightpoints2 = models.IntegerField(null=True)
    eightteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    eightpoints3 = models.IntegerField(null=True)
    eightteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    eightpoints4 = models.IntegerField(null=True)
    nineteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    ninepoints1 = models.IntegerField(null=True)
    nineteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    ninepoints2 = models.IntegerField(null=True)
    nineteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    ninepoints3 = models.IntegerField(null=True)
    nineteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    ninepoints4 = models.IntegerField(null=True)
    tenteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    tenpoints1 = models.IntegerField(null=True)
    tenteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    tenpoints2 = models.IntegerField(null=True)
    tenteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    tenpoints3 = models.IntegerField(null=True)
    tenteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    tenpoints4 = models.IntegerField(null=True)
    eleventeam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    elevenpoints1 = models.IntegerField(null=True)
    eleventeam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    elevenpoints2 = models.IntegerField(null=True)
    eleventeam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    elevenpoints3 = models.IntegerField(null=True)
    eleventeam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    elevenpoints4 = models.IntegerField(null=True)
    twelveteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twelvepoints1 = models.IntegerField(null=True)
    twelveteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twelvepoints2 = models.IntegerField(null=True)
    twelveteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twelvepoints3 = models.IntegerField(null=True)
    twelveteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    twelvepoints4 = models.IntegerField(null=True)
    thirteenteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    thirteenpoints1 = models.IntegerField(null=True)
    thirteenteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    thirteenpoints2 = models.IntegerField(null=True)
    thirteenteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    thirteenpoints3 = models.IntegerField(null=True)
    thirteenteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    thirteenpoints4 = models.IntegerField(null=True)
    fourteenteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourteenpoints1 = models.IntegerField(null=True)
    fourteenteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourteenpoints2 = models.IntegerField(null=True)
    fourteenteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourteenpoints3 = models.IntegerField(null=True)
    fourteenteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fourteenpoints4 = models.IntegerField(null=True)
    fifteenteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fifteenpoints1 = models.IntegerField(null=True)
    fifteenteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fifteenpoints2 = models.IntegerField(null=True)
    fifteenteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fifteenpoints3 = models.IntegerField(null=True)
    fifteenteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    fifteenpoints4 = models.IntegerField(null=True)
    sixteenteam1racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixteenpoints1 = models.IntegerField(null=True)
    sixteenteam2racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixteenpoints2 = models.IntegerField(null=True)
    sixteenteam3racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixteenpoints3 = models.IntegerField(null=True)
    sixteenteam4racer = models.CharField(null=True, max_length=50, choices=PLAYER_CHOICES)
    sixteenpoints4 = models.IntegerField(null=True)
    def __str__(self):
        return self.name






