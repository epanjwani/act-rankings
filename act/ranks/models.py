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
    LEAGUE_CHOICES = (
        ("A-League", "A-League"),
        ("C-League", "C-League"),
        ("N/A", "N/A"),
    )
    league = models.CharField(max_length=50, choices=LEAGUE_CHOICES, null=True)
    def __str__(self):
        return self.name

"""
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
        ("James Berthoud", "TJ"),
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
    T_CHOICES = (
        ("P1", "P1"),
        ("P2", "P2")
    )
    
    POINT_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3)
    )
    oneteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    onepoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    oneteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    onepoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    oneteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    onepoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    oneteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    onepoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twoteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twopoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twoteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twopoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twoteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twopoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twoteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twopoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    threeteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    threepoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    threeteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    threepoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    threeteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    threepoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    threeteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    threepoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fiveteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fivepoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fiveteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fivepoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fiveteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fivepoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fiveteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fivepoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    seventeam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sevenpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    seventeam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sevenpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    seventeam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sevenpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    seventeam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sevenpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eightteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    eightpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eightteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    eightpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eightteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    eightpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eightteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    eightpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    nineteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    ninepoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    nineteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    ninepoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    nineteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    ninepoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    nineteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    ninepoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    tenteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    tenpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    tenteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    tenpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    tenteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    tenpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    tenteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    tenpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eleventeam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    elevenpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eleventeam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    elevenpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eleventeam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    elevenpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    eleventeam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    elevenpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twelveteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twelvepoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twelveteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twelvepoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twelveteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twelvepoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    twelveteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    twelvepoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    thirteenteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    thirteenpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    thirteenteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    thirteenpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    thirteenteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    thirteenpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    thirteenteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    thirteenpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteenteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourteenpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteenteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourteenpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteenteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourteenpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fourteenteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fourteenpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fifteenteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fifteenpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fifteenteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fifteenpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fifteenteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fifteenpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    fifteenteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    fifteenpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteenteam1racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixteenpoints1 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteenteam2racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixteenpoints2 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteenteam3racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixteenpoints3 = models.IntegerField(null=True, choices=POINT_CHOICES)
    sixteenteam4racer = models.CharField(null=True, max_length=50, choices=T_CHOICES)
    sixteenpoints4 = models.IntegerField(null=True, choices=POINT_CHOICES)
    def __str__(self):
        return self.name

    """




