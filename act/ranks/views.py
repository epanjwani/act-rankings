from abc import abstractproperty
from django.shortcuts import render, redirect
from .models import Player, ACT, GlobalVariables
import openpyxl, math

# Create your views here.

#OVERALL STAT SETUP
def home(request):
    #players = ["Eashan Panjwani","Zach Bell","Benner Mullin","Jackson Brodwolf","Matt Halper","Alex Hazel","Harris Klein","Kohl Terry","Alex Mellas","Noah Paige","Julian Ricci","Robbie Kramer","Ethan Roberts","Henry Rogers","Ryan Simon","Peter Netchvolodoff","Andrew Schanuel","Avery Friedman","Josh Greenfield","Will Spartin","Will Goldberg","Brady Sheaffer","Aman Patil","Zach Stern","Josh Josef","Nico Simon", "Sam Schoepke", "James Berthoud","Jonathan Nurko", "Spencer Gladstone","Kion Noori", "Max Marchetto", "Chuck Leonetti", "Matt Flower", "Connor Caz", "Caleb Hughes", "Lukas Steinbock","Brian Volk"]
    player_dict = {}
    players = Player.objects.order_by('-elo')
    print("TEST")
    for player_object in players:
        print("uyay")
        if player_object.acts_ran > -1:
            player_dict[player_object.name] = player_object
        resetCounter = False
        if resetCounter == True:
            if (player_object.name == "Andrew Schanny" or player_object.name == "James Berthoud" or player_object.name == "Brian Volk" or player_object.name == "Josh Greenfield" or player_object.name == "Ethan Roberts" or player_object.name == "Will Spartin" or player_object.name == "Matt Halper"):
                player_object.elo = 1500
            elif (player_object.league == "A-League"):
                player_object.elo = 2000
            elif (player_object.league == "C-League"):
                player_object.elo = 1500
            else:
                player_object.elo = 1000
            player_object.acts_ran = 0
            player_object.elo_change = 0
            player_object.elo_change1 = 0
            player_object.elo_change2 = 0
            player_object.elo_change3 = 0
            player_object.elo_change4 = 0
            player_object.elo_change5 = 0
            player_object.total_points = 0
            player_object.accum_competitor_elo = 0
            player_object.save()
    return render(request, "ranks/home.html", {'dict': player_dict})

"""

def race(request):
    player_dict = {}
    players = Player.objects.order_by('-race rating') #add variable for race rating into player model
    for player_object in players:
        player_dict[player_object.name] = player_object
    return render(request, "ranks/race.html", {'dict': player_dict})

def player(request):
    race_dict = {}
    races = Race.objects
    for race_object in races:
        race_dict[race_object.name] = race_object
    return render(request, "ranks/player.html")

"""

#INDIVIDUAL ACT STAT SETUP
def enterTeamData(request):
    if "GET" == request.method:
        return render(request, 'ranks/teamData.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        # you may put validations here to check extension or file size
        wb = openpyxl.load_workbook(excel_file)
        # getting a particular sheet by name out of many sheets
        worksheet = wb.active
        print(worksheet)
        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        rowCount = 1
        team1player1 = 0
        team1player2 = 0
        team2player1 = 0
        team2player2 = 0
        team3player1 = 0
        team3player2 = 0
        team4player1 = 0
        team4player2 = 0
        team1player1name = ""
        team1player2name = ""
        team2player1name = ""
        team2player2name = ""
        team3player1name = ""
        team3player2name = ""
        team4player1name = ""
        team4player2name = ""
        team1character1name = ""
        team1character2name = ""
        team2character1name = ""
        team2character2name = ""
        team3character1name = ""
        team3character2name = ""
        team4character1name = ""
        team4character2name = ""

        player_dict = {
            "EP" : "Eashan Panjwani",
            "AS" : "Andrew Schanny",
            "PN" : "Peter Netch",
            "ZB" : "Zach Bell",
            "BM" : "Benner Mullin",
            "JB" : "Jackson Brodwolf",
            "MH" : "Matt Halper",
            "AH" : "Alex Hazel",
            "HK" : "Harris Klein",
            "KT" : "Kohl Terry",
            "AM" : "Alex Mellas",
            "NP" : "Noah Paige",
            "JR" : "Julian Ricci",
            "RK" : "Robbie Kramer",
            "ER" : "Ethan Roberts",
            "HR" : "Henry Rogers",
            "RS" : "Ryan Simon",
            "AF" : "Avery Friedman",
            "JG" : "Josh Greenfield",
            "WS" : "Will Spartin",
            "WG" : "Will Goldberg",
            "BS" : "Brady Sheaffer",
            "AP" : "Aman Patil",
            "ZS" : "Zach Stern",
            "NS" : "Nico Simon",
            "JJ" : "Josh Josef",
            "SS" : "Sam Schoepke",
            "TJ" : "James Berthoud",
            "JN" : "Jonathan Nurko",
            "SG" : "Spencer Gladstone",
            "KN" : "Kion Noori",
            "MM" : "Max Marchetto",
            "CL" : "Chuck Leonetti",
            "MF" : "Matt Flower",
            "CC" : "Connor Caz",
            "CH" : "Caleb Hughes",
            "LS" : "Lukas Steinbock",
            "BV" : "Brian Volk",
            "NSh" : "Nitan Shalon",
            "MZ" : "Mat Zlotnick",
            "GM" : "Gavin Morse"
        }

        act_object = ACT()
        t1player1_score = ""
        t1player2_score = ""
        t2player1_score = ""
        t2player2_score = ""
        t3player1_score = ""
        t3player2_score = ""
        t4player1_score = ""
        t4player2_score = ""

#READING EXCEL SHEET TO GET PLAYER POINTS
        for row in worksheet.iter_rows():
            if rowCount > 32:
                break
            if rowCount == 1 or rowCount == 2 or rowCount == 9 or rowCount == 10 or rowCount == 11 or rowCount == 12 or rowCount == 17 or rowCount == 18 or rowCount == 19 or rowCount == 20 or rowCount == 25 or rowCount == 26 or rowCount == 27 or rowCount == 28:
                rowCount+= 1
                continue
            rowCount+= 1
            row_data = list()
            cellCount = 1
            for cell in row:
                if cellCount == 1:
                    cellCount +=1 
                    continue
                row_data.append(str(cell.value))
                if rowCount == 4:
                    if cellCount == 3:
                        team1player1name = player_dict[str(cell.value)]
                    if cellCount == 4:
                        team1player2name = player_dict[str(cell.value)]
                    if cellCount == 5:
                        team2player1name = player_dict[str(cell.value)]
                    if cellCount == 6:
                        team2player2name = player_dict[str(cell.value)]
                    if cellCount == 7:
                        team3player1name = player_dict[str(cell.value)]
                    if cellCount == 8:
                        team3player2name = player_dict[str(cell.value)]
                    if cellCount == 9:
                        team4player1name = player_dict[str(cell.value)]
                    if cellCount == 10:
                        team4player2name = player_dict[str(cell.value)]
                if rowCount == 5:
                    if cellCount == 3:
                        team1character1name = str(cell.value)
                    if cellCount == 4:
                        team1character2name = str(cell.value)
                    if cellCount == 5:
                        team2character1name = str(cell.value)
                    if cellCount == 6:
                        team2character2name = str(cell.value)
                    if cellCount == 7:
                        team3character1name = str(cell.value)
                    if cellCount == 8:
                        team3character2name = str(cell.value)
                    if cellCount == 9:
                        team4character1name = str(cell.value)
                    if cellCount == 10:
                        team4character2name = str(cell.value)
                if rowCount != 4 and rowCount != 5:
                    if cellCount == 3: 
                        if cell.value != None:
                            team1player1 += int(cell.value)
                            t1player1_score += str(cell.value)
                        else:
                            t1player1_score += "null"
                        t1player1_score += ","
                    if cellCount == 4: 
                        if cell.value != None:
                            team1player2 += int(cell.value)
                            t1player2_score += str(cell.value)
                        else:
                            t1player2_score += "null"
                        t1player2_score += ","
                    if cellCount == 5: 
                        if cell.value != None:
                            team2player1 += int(cell.value)
                            t2player1_score += str(cell.value)
                        else:
                            t2player1_score += "null"
                        t2player1_score += ","
                    if cellCount == 6: 
                        if cell.value != None:
                            team2player2 += int(cell.value)
                            t2player2_score += str(cell.value)
                        else:
                            t2player2_score += "null"
                        t2player2_score += ","
                    if cellCount == 7: 
                        if cell.value != None:
                            team3player1 += int(cell.value)
                            t3player1_score += str(cell.value)
                        else:
                            t3player1_score += "null"
                        t3player1_score += ","
                    if cellCount == 8: 
                        if cell.value != None:
                            team3player2 += int(cell.value)
                            t3player2_score += str(cell.value)
                        else:
                            t3player2_score += "null"
                        t3player2_score += ","
                    if cellCount == 9:
                        if cell.value != None:
                            team4player1 += int(cell.value)
                            t4player1_score += str(cell.value)
                        else:
                            t4player1_score += "null"
                        t4player1_score += ","
                    if cellCount == 10: 
                        if cell.value != None:
                            team4player2 += int(cell.value)
                            t4player2_score += str(cell.value)
                        else:
                            t4player2_score += "null"
                        t4player2_score += ","
                if cellCount >= 10:
                    break
                cellCount+=1
            excel_data.append(row_data)
        print(team1player1)
        print(team1player2)
        print(team2player1)
        print(team2player2)
        print(team3player1)
        print(team3player2)
        print(team4player1)
        print(team4player2)

#CONNECT PLAYER SCORES TO THE RESPECTIVE PLAYER MODEL
        t1p1 = Player.objects.get(name=team1player1name)
        t1p2 = Player.objects.get(name=team1player2name)
        t2p1 = Player.objects.get(name=team2player1name)
        t2p2 = Player.objects.get(name=team2player2name)
        t3p1 = Player.objects.get(name=team3player1name)
        t3p2 = Player.objects.get(name=team3player2name)
        t4p1 = Player.objects.get(name=team4player1name)
        t4p2 = Player.objects.get(name=team4player2name)

#UPDATE ACT MODEL
    #UPDATE PLAYERS

        act_object.t1player1 = t1p1
        act_object.t1player2 = t1p2
        act_object.t2player1 = t2p1
        act_object.t2player2 = t2p2
        act_object.t3player1 = t3p1
        act_object.t3player2 = t3p2
        act_object.t4player1 = t4p1
        act_object.t4player2 = t4p2
    #UPDATE CHARACTERS
        act_object.t1character1 = team1character1name
        act_object.t1character2 = team1character2name
        act_object.t2character1 = team2character1name
        act_object.t2character2 = team2character2name
        act_object.t3character1 = team3character1name
        act_object.t3character2 = team3character2name
        act_object.t4character1 = team4character1name
        act_object.t4character2 = team4character2name
    #UPDATE SC
        act_object.t1player1_sc = team1player1
        act_object.t1player2_sc = team1player2
        act_object.t2player1_sc = team2player1
        act_object.t2player2_sc = team2player2
        act_object.t3player1_sc = team3player1
        act_object.t3player2_sc = team3player2
        act_object.t4player1_sc = team4player1
        act_object.t4player2_sc = team4player2
    #UPDATE SCORES
        act_object.t1player1_scores = t1player1_score
        act_object.t1player2_scores = t1player2_score
        act_object.t2player1_scores = t2player1_score
        act_object.t2player2_scores = t2player2_score
        act_object.t3player1_scores = t3player1_score
        act_object.t3player2_scores = t3player2_score
        act_object.t4player1_scores = t4player1_score
        act_object.t4player2_scores = t4player2_score
    ###############WE NEED TO FINISH UPDATING ACT OBJECT. THINK ABOUT HOW TO ACCOUNT FOR BLANK CHARACTER FIELDS IN EXCEL

#ADJ ELO

        team1zscore = 0
        team2zscore = 0
        team3zscore = 0
        team4zscore = 0
        t1combo = ""
        t2combo = ""
        t3combo = ""
        t4combo = ""
        t1combocount = ""
        t2combocount = ""
        t3combocount = ""
        t4combocount = ""
        ###### CHANGE ARRAYS TO MAPS ( and update the stuff below and in new z-score area ) #########

        overall = GlobalVariables.objects.first()

        print(overall.toad_bowser)
        if (team1character1name == "T" and team1character2name == "BJ"):
            team1zscore = overall.toad_bowser
            t1combo = 'toad_bowser'
            t1combocount = 'toad_bowser_count'
        elif (team1character1name == "T" and team1character2name == "DK"):
            team1zscore = overall.toad_diddy
            t1combo = 'toad_diddy'
            t1combocount = 'toad_diddy_count'
        elif (team1character1name == "T" and team1character2name == "K"):
            team1zscore = overall.toad_koopa
            t1combo = 'toad_koopa'
            t1combocount = 'toad_koopa_count'
        elif (team1character1name == "T" and team1character2name == "B"):
            team1zscore = overall.toad_baby
            t1combo = 'toad_baby'
            t1combocount = 'toad_baby_count'
        elif (team1character1name == "BJ" and team1character2name == "DK"):
            team1zscore = overall.bowser_diddy
            t1combo = 'bowser_diddy'
            t1combocount = 'bowser_diddy_count'
        elif (team1character1name == "BJ" and team1character2name == "K"):
            team1zscore = overall.bowser_koopa
            t1combo = 'bowser_koopa'
            t1combocount = 'bowser_koopa_count'
        elif (team1character1name == "BJ" and team1character2name == "B"):
            team1zscore = overall.bowser_baby
            t1combo = 'bowser_baby'
            t1combocount = 'bowser_baby_count'
        elif (team1character1name == "DK" and team1character2name == "K"):
            team1zscore = overall.diddy_koopa
            t1combo = 'diddy_koopa'
            t1combocount = 'diddy_koopa_count'
        elif (team1character1name == "DK" and team1character2name == "B"):
            team1zscore = overall.diddy_baby
            t1combo = 'diddy_baby'
            t1combocount = 'diddy_baby_count'
        elif (team1character1name == "K" and team1character2name == "B"):
            team1zscore = overall.koopa_baby
            t1combo = 'koopa_baby'
            t1combocount = 'koopa_baby_count'
        elif (team1character1name == "K" and team1character2name == "K"):
            team1zscore = overall.koopa_koopa
            t1combo = 'koopa_koopa'
            t1combocount = 'koopa_koopa_count'
        elif (team1character1name == "B" and team1character2name == "B"):
            team1zscore = overall.baby_baby
            t1combo = 'baby_baby'
            t1combocount = 'baby_baby_count'

        if (team2character1name == "T" and team2character2name == "BJ"):
            team2zscore = overall.toad_bowser
            t2combo = 'toad_bowser'
            t2combocount = 'toad_bowser_count'
        elif (team2character1name == "T" and team2character2name == "DK"):
            team2zscore = overall.toad_diddy
            t2combo = 'toad_diddy'
            t2combocount = 'toad_diddy_count'
        elif (team2character1name == "T" and team2character2name == "K"):
            team2zscore = overall.toad_koopa
            t2combo = 'toad_koopa'
            t2combocount = 'toad_koopa_count'
        elif (team2character1name == "T" and team2character2name == "B"):
            team2zscore = overall.toad_baby
            t2combo = 'toad_baby'
            t2combocount = 'toad_baby_count'
        elif (team2character1name == "BJ" and team2character2name == "DK"):
            team2zscore = overall.bowser_diddy
            t2combo = 'bowser_diddy'
            t2combocount = 'bowser_diddy_count'
        elif (team2character1name == "BJ" and team2character2name == "K"):
            team2zscore = overall.bowser_koopa
            t2combo = 'bowser_koopa'
            t2combocount = 'bowser_koopa_count'
        elif (team2character1name == "BJ" and team2character2name == "B"):
            team2zscore = overall.bowser_baby
            t2combo = 'bowser_baby'
            t2combocount = 'bowser_baby_count'
        elif (team2character1name == "DK" and team2character2name == "K"):
            team2zscore = overall.diddy_koopa
            t2combo = 'diddy_koopa'
            t2combocount = 'diddy_koopa_count'
        elif (team2character1name == "DK" and team2character2name == "B"):
            team2zscore = overall.diddy_baby
            t2combo = 'diddy_baby'
            t2combocount = 'diddy_baby_count'
        elif (team2character1name == "K" and team2character2name == "B"):
            team2zscore = overall.koopa_baby
            t2combo = 'koopa_baby'
            t2combocount = 'koopa_baby_count'
        elif (team2character1name == "K" and team2character2name == "K"):
            team2zscore = overall.koopa_koopa
            t2combo = 'koopa_koopa'
            t2combocount = 'koopa_koopa_count'
        elif (team2character1name == "B" and team2character2name == "B"):
            team2zscore = overall.baby_baby
            t2combo = 'baby_baby'
            t2combocount = 'baby_baby_count'

        if (team3character1name == "T" and team3character2name == "BJ"):
            team3zscore = overall.toad_bowser
            t3combo = 'toad_bowser'
            t3combocount = 'toad_bowser_count'
        elif (team3character1name == "T" and team3character2name == "DK"):
            team3zscore = overall.toad_diddy
            t3combo = 'toad_diddy'
            t3combocount = 'toad_diddy_count'
        elif (team3character1name == "T" and team3character2name == "K"):
            team3zscore = overall.toad_koopa
            t3combo = 'toad_koopa'
            t3combocount = 'toad_koopa_count'
        elif (team3character1name == "T" and team3character2name == "B"):
            team3zscore = overall.toad_baby
            t3combo = 'toad_baby'
            t3combocount = 'toad_baby_count'
        elif (team3character1name == "BJ" and team3character2name == "DK"):
            team3zscore = overall.bowser_diddy
            t3combo = 'bowser_diddy'
            t3combocount = 'bowser_diddy_count'
        elif (team3character1name == "BJ" and team3character2name == "K"):
            team3zscore = overall.bowser_koopa
            t3combo = 'bowser_koopa'
            t3combocount = 'bowser_koopa_count'
        elif (team3character1name == "BJ" and team3character2name == "B"):
            team3zscore = overall.bowser_baby
            t3combo = 'bowser_baby'
            t3combocount = 'bowser_baby_count'
        elif (team3character1name == "DK" and team3character2name == "K"):
            team3zscore = overall.diddy_koopa
            t3combo = 'diddy_koopa'
            t3combocount = 'diddy_koopa_count'
        elif (team3character1name == "DK" and team3character2name == "B"):
            team3zscore = overall.diddy_baby
            t3combo = 'diddy_baby'
            t3combocount = 'diddy_baby_count'
        elif (team3character1name == "K" and team3character2name == "B"):
            team3zscore = overall.koopa_baby
            t3combo = 'koopa_baby'
            t3combocount = 'koopa_baby_count'
        elif (team3character1name == "K" and team3character2name == "K"):
            team3zscore = overall.koopa_koopa
            t3combo = 'koopa_koopa'
            t3combocount = 'koopa_koopa_count'
        elif (team3character1name == "B" and team3character2name == "B"):
            team3zscore = overall.baby_baby
            t3combo = 'baby_baby'
            t3combocount = 'baby_baby_count'

        if (team4character1name == "T" and team4character2name == "BJ"):
            team4zscore = overall.toad_bowser
            t4combo = 'toad_bowser'
            t4combocount = 'toad_bowser_count'
        elif (team4character1name == "T" and team4character2name == "DK"):
            team4zscore = overall.toad_diddy
            t4combo = 'toad_diddy'
            t4combocount = 'toad_diddy_count'
        elif (team4character1name == "T" and team4character2name == "K"):
            team4zscore = overall.toad_koopa
            t4combo = 'toad_koopa'
            t4combocount = 'toad_koopa_count'
        elif (team4character1name == "T" and team4character2name == "B"):
            team4zscore = overall.toad_baby
            t4combo = 'toad_baby'
            t4combocount = 'toad_baby_count'
        elif (team4character1name == "BJ" and team4character2name == "DK"):
            team4zscore = overall.bowser_diddy
            t4combo = 'bowser_diddy'
            t4combocount = 'bowser_diddy_count'
        elif (team4character1name == "BJ" and team4character2name == "K"):
            team4zscore = overall.bowser_koopa
            t4combo = 'bowser_koopa'
            t4combocount = 'bowser_koopa_count'
        elif (team4character1name == "BJ" and team4character2name == "B"):
            team4zscore = overall.bowser_baby
            t4combo = 'bowser_baby'
            t4combocount = 'bowser_baby_count'
        elif (team4character1name == "DK" and team4character2name == "K"):
            team4zscore = overall.diddy_koopa
            t4combo = 'diddy_koopa'
            t4combocount = 'diddy_koopa_count'
        elif (team4character1name == "DK" and team4character2name == "B"):
            team4zscore = overall.diddy_baby
            t4combo = 'diddy_baby'
            t4combocount = 'diddy_baby_count'
        elif (team4character1name == "K" and team4character2name == "B"):
            team4zscore = overall.koopa_baby
            t4combo = 'koopa_baby'
            t4combocount = 'koopa_baby_count'
        elif (team4character1name == "K" and team4character2name == "K"):
            team4zscore = overall.koopa_koopa
            t4combo = 'koopa_koopa'
            t4combocount = 'koopa_koopa_count'
        elif (team4character1name == "B" and team4character2name == "B"):
            team4zscore = overall.baby_baby
            t4combo = 'baby_baby'
            t4combocount = 'baby_baby_count'

        character_combo_array = [t1combo, t2combo, t3combo, t4combo]
        character_combo_count_array = [t1combocount, t2combocount, t3combocount, t4combocount]

        #Calculated elo distribution sd
        elo_distribution_sd = 118.2991
        print("team z scores")
        print(team1zscore)
        print(team2zscore)
        print(team3zscore)
        print(team4zscore)
        if (overall.score_count < 80):
            t1p1_adj_elo = t1p1.elo
            t1p2_adj_elo = t1p2.elo
            t2p1_adj_elo = t2p1.elo
            t2p2_adj_elo = t2p2.elo
            t3p1_adj_elo = t3p1.elo
            t3p2_adj_elo = t3p2.elo
            t4p1_adj_elo = t4p1.elo
            t4p2_adj_elo = t4p2.elo
        else:
            t1p1_adj_elo = t1p1.elo + elo_distribution_sd*team1zscore
            t1p2_adj_elo = t1p2.elo + elo_distribution_sd*team1zscore
            t2p1_adj_elo = t2p1.elo + elo_distribution_sd*team2zscore
            t2p2_adj_elo = t2p2.elo + elo_distribution_sd*team2zscore
            t3p1_adj_elo = t3p1.elo + elo_distribution_sd*team3zscore
            t3p2_adj_elo = t3p2.elo + elo_distribution_sd*team3zscore
            t4p1_adj_elo = t4p1.elo + elo_distribution_sd*team4zscore
            t4p2_adj_elo = t4p2.elo + elo_distribution_sd*team4zscore

        print("elo dist sd")
        print(elo_distribution_sd)
        print("adj elo")
        print(t1p1_adj_elo)
        print(t1p2_adj_elo)
        print(t2p1_adj_elo)
        print(t2p2_adj_elo)
        print(t3p1_adj_elo)
        print(t3p2_adj_elo)
        print(t4p1_adj_elo)
        print(t4p2_adj_elo)

#CALCULATE TEAM, COMPETITOR ELOS
        t1_elo = (t1p1_adj_elo + t1p2_adj_elo)/2
        t2_elo = (t2p1_adj_elo + t2p2_adj_elo)/2
        t3_elo = (t3p1_adj_elo + t3p2_adj_elo)/2
        t4_elo = (t4p1_adj_elo + t4p2_adj_elo)/2
        t1Comp = (t2_elo + t3_elo + t4_elo)/3
        t2Comp = (t1_elo + t3_elo + t4_elo)/3
        t3Comp = (t1_elo + t2_elo + t4_elo)/3
        t4Comp = (t1_elo + t2_elo + t3_elo)/3

        t1Comp_unadj = (t2p1.elo + t2p2.elo + t3p1.elo + t3p2.elo + t4p1.elo + t4p2.elo)/6
        t2Comp_unadj = (t1p1.elo + t1p2.elo + t3p1.elo + t3p2.elo + t4p1.elo + t4p2.elo)/6
        t3Comp_unadj = (t1p1.elo + t1p2.elo + t2p1.elo + t2p2.elo + t4p1.elo + t4p2.elo)/6
        t4Comp_unadj = (t1p1.elo + t1p2.elo + t2p1.elo + t2p2.elo + t3p1.elo + t3p2.elo)/6

#EXPECTED POINTS
        t1p1_exp_pts_z = (t1p1_adj_elo - t1Comp)/elo_distribution_sd
        t1p2_exp_pts_z = (t1p2_adj_elo - t1Comp)/elo_distribution_sd
        t2p1_exp_pts_z = (t2p1_adj_elo - t2Comp)/elo_distribution_sd
        t2p2_exp_pts_z = (t2p2_adj_elo - t2Comp)/elo_distribution_sd
        t3p1_exp_pts_z = (t3p1_adj_elo - t3Comp)/elo_distribution_sd
        t3p2_exp_pts_z = (t3p2_adj_elo - t3Comp)/elo_distribution_sd
        t4p1_exp_pts_z = (t4p1_adj_elo - t4Comp)/elo_distribution_sd
        t4p2_exp_pts_z = (t4p2_adj_elo - t4Comp)/elo_distribution_sd

        t1p1_exp_pts_z_unadj = (t1p1.elo - t1Comp_unadj)/elo_distribution_sd
        t1p2_exp_pts_z_unadj = (t1p2.elo - t1Comp_unadj)/elo_distribution_sd
        t2p1_exp_pts_z_unadj = (t2p1.elo - t2Comp_unadj)/elo_distribution_sd
        t2p2_exp_pts_z_unadj = (t2p2.elo - t2Comp_unadj)/elo_distribution_sd
        t3p1_exp_pts_z_unadj = (t3p1.elo - t3Comp_unadj)/elo_distribution_sd
        t3p2_exp_pts_z_unadj = (t3p2.elo - t3Comp_unadj)/elo_distribution_sd
        t4p1_exp_pts_z_unadj = (t4p1.elo - t4Comp_unadj)/elo_distribution_sd
        t4p2_exp_pts_z_unadj = (t4p2.elo - t4Comp_unadj)/elo_distribution_sd

        print("exp pts_z")
        print(t1p1_exp_pts_z)
        print(t1p2_exp_pts_z)
        print(t2p1_exp_pts_z)
        print(t2p2_exp_pts_z)
        print(t3p1_exp_pts_z)
        print(t3p2_exp_pts_z)
        print(t4p1_exp_pts_z)
        print(t4p2_exp_pts_z)

        t1p1_exp_pts_raw = t1p1_exp_pts_z*overall.score_sd + 12
        t1p2_exp_pts_raw = t1p2_exp_pts_z*overall.score_sd + 12
        t2p1_exp_pts_raw = t2p1_exp_pts_z*overall.score_sd + 12
        t2p2_exp_pts_raw = t2p2_exp_pts_z*overall.score_sd + 12
        t3p1_exp_pts_raw = t3p1_exp_pts_z*overall.score_sd + 12
        t3p2_exp_pts_raw = t3p2_exp_pts_z*overall.score_sd + 12
        t4p1_exp_pts_raw = t4p1_exp_pts_z*overall.score_sd + 12
        t4p2_exp_pts_raw = t4p2_exp_pts_z*overall.score_sd + 12

        t1p1_exp_pts_raw_unadj = t1p1_exp_pts_z_unadj*overall.score_sd + 12
        t1p2_exp_pts_raw_unadj = t1p2_exp_pts_z_unadj*overall.score_sd + 12
        t2p1_exp_pts_raw_unadj = t2p1_exp_pts_z_unadj*overall.score_sd + 12
        t2p2_exp_pts_raw_unadj = t2p2_exp_pts_z_unadj*overall.score_sd + 12
        t3p1_exp_pts_raw_unadj = t3p1_exp_pts_z_unadj*overall.score_sd + 12
        t3p2_exp_pts_raw_unadj = t3p2_exp_pts_z_unadj*overall.score_sd + 12
        t4p1_exp_pts_raw_unadj = t4p1_exp_pts_z_unadj*overall.score_sd + 12
        t4p2_exp_pts_raw_unadj = t4p2_exp_pts_z_unadj*overall.score_sd + 12
        
        print("score sd")
        print(overall.score_sd)
        print("exp pts raw")
        print(t1p1_exp_pts_raw)
        print(t1p2_exp_pts_raw)
        print(t2p1_exp_pts_raw)
        print(t2p2_exp_pts_raw)
        print(t3p1_exp_pts_raw)
        print(t3p2_exp_pts_raw)
        print(t4p1_exp_pts_raw)
        print(t4p2_exp_pts_raw)

        t1p1_exp_pts = t1p1_exp_pts_raw*(48/(36+t1p1_exp_pts_raw))
        t1p2_exp_pts = t1p2_exp_pts_raw*(48/(36+t1p2_exp_pts_raw))
        t2p1_exp_pts = t2p1_exp_pts_raw*(48/(36+t2p1_exp_pts_raw))
        t2p2_exp_pts = t2p2_exp_pts_raw*(48/(36+t2p2_exp_pts_raw))
        t3p1_exp_pts = t3p1_exp_pts_raw*(48/(36+t3p1_exp_pts_raw))
        t3p2_exp_pts = t3p2_exp_pts_raw*(48/(36+t3p2_exp_pts_raw))
        t4p1_exp_pts = t4p1_exp_pts_raw*(48/(36+t4p1_exp_pts_raw))
        t4p2_exp_pts = t4p2_exp_pts_raw*(48/(36+t4p2_exp_pts_raw))

        t1p1_exp_pts_unadj = t1p1_exp_pts_raw_unadj*(48/(36+t1p1_exp_pts_raw_unadj))
        t1p2_exp_pts_unadj = t1p2_exp_pts_raw_unadj*(48/(36+t1p2_exp_pts_raw_unadj))
        t2p1_exp_pts_unadj = t2p1_exp_pts_raw_unadj*(48/(36+t2p1_exp_pts_raw_unadj))
        t2p2_exp_pts_unadj = t2p2_exp_pts_raw_unadj*(48/(36+t2p2_exp_pts_raw_unadj))
        t3p1_exp_pts_unadj = t3p1_exp_pts_raw_unadj*(48/(36+t3p1_exp_pts_raw_unadj))
        t3p2_exp_pts_unadj = t3p2_exp_pts_raw_unadj*(48/(36+t3p2_exp_pts_raw_unadj))
        t4p1_exp_pts_unadj = t4p1_exp_pts_raw_unadj*(48/(36+t4p1_exp_pts_raw_unadj))
        t4p2_exp_pts_unadj = t4p2_exp_pts_raw_unadj*(48/(36+t4p2_exp_pts_raw_unadj))

        exp_pts_unadj_array = [t1p1_exp_pts_unadj,t1p2_exp_pts_unadj,t2p1_exp_pts_unadj,t2p2_exp_pts_unadj,t3p1_exp_pts_unadj,t3p2_exp_pts_unadj,t4p1_exp_pts_unadj,t4p2_exp_pts_unadj]

        print("exp pts")
        print(t1p1_exp_pts)
        print(t1p2_exp_pts)
        print(t2p1_exp_pts)
        print(t2p2_exp_pts)
        print(t3p1_exp_pts)
        print(t3p2_exp_pts)
        print(t4p1_exp_pts)
        print(t4p2_exp_pts)

#TEAM POINTS
        t1_points = team1player1 + team1player2
        t2_points = team2player1 + team2player2
        t3_points = team3player1 + team3player2
        t4_points = team4player1 + team4player2
#ELOCHANGE SETUP
        t1_elochange = 0
        t2_elochange = 0
        t3_elochange = 0
        t4_elochange = 0
        t1p1_elochange = 0
        t1p2_elochange = 0
        t2p1_elochange = 0
        t2p2_elochange = 0
        t3p1_elochange = 0
        t3p2_elochange = 0
        t4p1_elochange = 0
        t4p2_elochange = 0

#CHANGES IN TEAMMATE ELO, COMPETITOR ELO
        """    
        Competitor elo is changed lower down right now, but teammate elo has to be updated before the results affect elo, so we should move both stats up here for clarity
        ***THIS DATA HAS ADJUSTED ELO FROM CHARACTERS NOW -- DO WE WANT THAT
        
        t1p1.accum_competitor_elo += t1Comp
        t1p2.accum_competitor_elo += t1Comp
        t2p1.accum_competitor_elo += t2Comp
        t2p2.accum_competitor_elo += t2Comp
        t3p1.accum_competitor_elo += t3Comp
        t3p2.accum_competitor_elo += t3Comp
        t4p1.accum_competitor_elo += t4Comp
        t4p2.accum_competitor_elo += t4Comp
        
        t1p1.accum_teammate_elo += t1p2.elo
        t1p2.accum_teammate_elo += t1p1.elo
        t2p1.accum_teammate_elo += t2p2.elo
        t2p2.accum_teammate_elo += t2p1.elo
        t3p1.accum_teammate_elo += t3p2.elo
        t3p2.accum_teammate_elo += t3p1.elo
        t4p1.accum_teammate_elo += t4p2.elo
        t4p2.accum_teammate_elo += t4p1.elo
        """
        
#CALCULATING INDIV ELO CHANGES
        t1p1_elochange += (team1player1 - t1p1_exp_pts)*2*(((abs(team1player1 - t1p1_exp_pts))**0.8)/6.9)*3
        t1p2_elochange += (team1player2 - t1p2_exp_pts)*2*(((abs(team1player2 - t1p2_exp_pts))**0.8)/6.9)*3
        t2p1_elochange += (team2player1 - t2p1_exp_pts)*2*(((abs(team2player1 - t2p1_exp_pts))**0.8)/6.9)*3
        t2p2_elochange += (team2player2 - t2p2_exp_pts)*2*(((abs(team2player2 - t2p2_exp_pts))**0.8)/6.9)*3
        t3p1_elochange += (team3player1 - t3p1_exp_pts)*2*(((abs(team3player1 - t3p1_exp_pts))**0.8)/6.9)*3
        t3p2_elochange += (team3player2 - t3p2_exp_pts)*2*(((abs(team3player2 - t3p2_exp_pts))**0.8)/6.9)*3
        t4p1_elochange += (team4player1 - t4p1_exp_pts)*2*(((abs(team4player1 - t4p1_exp_pts))**0.8)/6.9)*3
        t4p2_elochange += (team4player2 - t4p2_exp_pts)*2*(((abs(team4player2 - t4p2_exp_pts))**0.8)/6.9)*3
        
        print("indiv elochange")
        print(t1p1_elochange)
        print(t1p2_elochange)
        print(t2p1_elochange)
        print(t2p2_elochange)
        print(t3p1_elochange)
        print(t3p2_elochange)
        print(t4p1_elochange)
        print(t4p2_elochange)

#CALCULATING TEAM ELO CHANGES
        if(t1_points != t2_points):
            point_diff = abs(t1_points-t2_points)
            result = 1
            if t1_points < t2_points:
                result = 0

            mov = ((point_diff + 3)**0.8)/6.9
            p_win = 1/(1+(10**((t2_elo-t1_elo)/400)))
            change = (mov*20*(result-p_win))

            t1_elochange += change
            t2_elochange -= change

        if(t1_points != t3_points):
            point_diff = abs(t1_points-t3_points)
            result = 1
            if t1_points < t3_points:
                result = 0

            mov = ((point_diff + 3)**0.8)/6.9
            p_win = 1/(1+(10**((t3_elo-t1_elo)/400)))
            change = (mov*20*(result-p_win))
           
            t1_elochange += change
            t3_elochange -= change

        if(t1_points != t4_points):
            point_diff = abs(t1_points-t4_points)
            result = 1
            if t1_points < t4_points:
                result = 0           

            mov = ((point_diff + 3)**0.8)/6.9
            p_win = 1/(1+(10**((t4_elo-t1_elo)/400)))
            change = (mov*20*(result-p_win))            

            t1_elochange += change
            t4_elochange -= change

        if(t2_points != t3_points):
            point_diff = abs(t2_points-t3_points)
            result = 1
            if t2_points < t3_points:
                result = 0           

            mov = ((point_diff + 3)**0.8)/6.9
            p_win = 1/(1+(10**((t3_elo-t2_elo)/400)))
            change = (mov*20*(result-p_win))

            t2_elochange += change
            t3_elochange -= change

        if(t2_points != t4_points):
            point_diff = abs(t2_points-t4_points)
            result = 1
            if t2_points < t4_points:
                result = 0

            mov = ((point_diff + 3)**0.8)/6.9
            p_win = 1/(1+(10**((t4_elo-t2_elo)/400)))
            change = (mov*20*(result-p_win))

            t2_elochange += change
            t4_elochange -= change

        if(t3_points != t4_points):
            point_diff = abs(t3_points-t4_points)
            result = 1
            if t3_points < t4_points:
                result = 0

            mov = ((point_diff + 3)**0.8)/6.9
            p_win = 1/(1+(10**((t4_elo-t3_elo)/400)))
            change = (mov*20*(result-p_win))

            t3_elochange += change
            t4_elochange -= change

#T1P1 elo, total act, total points, last 5 act updates
        t1p1_elochange = (t1p1_elochange + t1_elochange)/2 #adds team change to indiv change and averages
        t1p1.elo += t1p1_elochange

        t1p1.elo_change5 = t1p1.elo_change4
        t1p1.elo_change4 = t1p1.elo_change3
        t1p1.elo_change3 = t1p1.elo_change2
        t1p1.elo_change2 = t1p1.elo_change1
        t1p1.elo_change1 = t1p1_elochange
        t1p1.elo_change = t1p1.elo_change1+ t1p1.elo_change2+ t1p1.elo_change3+ t1p1.elo_change4+ t1p1.elo_change5
        
        t1p1.acts_ran += 1
        t1p1.total_points += team1player1
        t1p1.accum_competitor_elo += t1Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t1p1.save()

#T1P2 elo, total act, total points, last 5 act updates
        t1p2_elochange = (t1p2_elochange + t1_elochange)/2 #adds team change to indiv change and averages
        t1p2.elo += t1p2_elochange
        
        t1p2.elo_change5 = t1p2.elo_change4
        t1p2.elo_change4 = t1p2.elo_change3
        t1p2.elo_change3 = t1p2.elo_change2
        t1p2.elo_change2 = t1p2.elo_change1
        t1p2.elo_change1 = t1p2_elochange
        t1p2.elo_change = t1p2.elo_change1+ t1p2.elo_change2+ t1p2.elo_change3+ t1p2.elo_change4+ t1p2.elo_change5

        t1p2.acts_ran += 1
        t1p2.total_points += team1player2
        t1p2.accum_competitor_elo += t1Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t1p2.save()

#T2P1 elo, total act, total points, last 5 act updates
        t2p1_elochange = (t2p1_elochange + t2_elochange)/2 #adds team change to indiv change and averages
        t2p1.elo += t2p1_elochange
        
        t2p1.elo_change5 = t2p1.elo_change4
        t2p1.elo_change4 = t2p1.elo_change3
        t2p1.elo_change3 = t2p1.elo_change2
        t2p1.elo_change2 = t2p1.elo_change1
        t2p1.elo_change1 = t2p1_elochange
        t2p1.elo_change = t2p1.elo_change1+ t2p1.elo_change2+ t2p1.elo_change3+ t2p1.elo_change4+ t2p1.elo_change5
    
        t2p1.acts_ran += 1
        t2p1.total_points += team2player1
        t2p1.accum_competitor_elo += t2Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t2p1.save()

#T2P2 elo, total act, total points, last 5 act updates
        t2p2_elochange = (t2p2_elochange + t2_elochange)/2 #adds team change to indiv change and averages
        t2p2.elo += t2p2_elochange
        
        t2p2.elo_change5 = t2p2.elo_change4
        t2p2.elo_change4 = t2p2.elo_change3
        t2p2.elo_change3 = t2p2.elo_change2
        t2p2.elo_change2 = t2p2.elo_change1
        t2p2.elo_change1 = t2p2_elochange
        t2p2.elo_change = t2p2.elo_change1+ t2p2.elo_change2+ t2p2.elo_change3+ t2p2.elo_change4+ t2p2.elo_change5

        t2p2.acts_ran += 1
        t2p2.total_points += team2player2
        t2p2.accum_competitor_elo += t2Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t2p2.save()

#T3P1 elo, total act, total points, last 5 act updates
        t3p1_elochange = (t3p1_elochange + t3_elochange)/2 #adds team change to indiv change and averages
        t3p1.elo += t3p1_elochange
        
        t3p1.elo_change5 = t3p1.elo_change4
        t3p1.elo_change4 = t3p1.elo_change3
        t3p1.elo_change3 = t3p1.elo_change2
        t3p1.elo_change2 = t3p1.elo_change1
        t3p1.elo_change1 = t3p1_elochange
        t3p1.elo_change = t3p1.elo_change1+ t3p1.elo_change2+ t3p1.elo_change3+ t3p1.elo_change4+ t3p1.elo_change5
        
        t3p1.acts_ran += 1
        t3p1.total_points += team3player1
        t3p1.accum_competitor_elo += t3Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t3p1.save()

#T3P2 elo, total act, total points, last 5 act updates
        t3p2_elochange = (t3p2_elochange + t3_elochange)/2 #adds team change to indiv change and averages
        t3p2.elo += t3p2_elochange
        
        t3p2.elo_change5 = t3p2.elo_change4
        t3p2.elo_change4 = t3p2.elo_change3
        t3p2.elo_change3 = t3p2.elo_change2
        t3p2.elo_change2 = t3p2.elo_change1
        t3p2.elo_change1 = t3p2_elochange
        t3p2.elo_change = t3p2.elo_change1+ t3p2.elo_change2+ t3p2.elo_change3+ t3p2.elo_change4+ t3p2.elo_change5
        
        t3p2.acts_ran += 1
        t3p2.total_points += team3player2
        t3p2.accum_competitor_elo += t3Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t3p2.save()

#T4P1 elo, total act, total points, last 5 act updates
        t4p1_elochange = (t4p1_elochange + t4_elochange)/2 #adds team change to indiv change and averages
        t4p1.elo += t4p1_elochange

        t4p1.elo_change5 = t4p1.elo_change4
        t4p1.elo_change4 = t4p1.elo_change3
        t4p1.elo_change3 = t4p1.elo_change2
        t4p1.elo_change2 = t4p1.elo_change1
        t4p1.elo_change1 = t4p1_elochange
        t4p1.elo_change = t4p1.elo_change1+ t4p1.elo_change2+ t4p1.elo_change3+ t4p1.elo_change4+ t4p1.elo_change5
        
        t4p1.acts_ran += 1
        t4p1.total_points += team4player1
        t4p1.accum_competitor_elo += t4Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t4p1.save()

#T4P2 elo, total act, total points, last 5 act updates
        t4p2_elochange = (t4p2_elochange + t4_elochange)/2 #adds team change to indiv change and averages
        t4p2.elo += t4p2_elochange
        
        t4p2.elo_change5 = t4p2.elo_change4
        t4p2.elo_change4 = t4p2.elo_change3
        t4p2.elo_change3 = t4p2.elo_change2
        t4p2.elo_change2 = t4p2.elo_change1
        t4p2.elo_change1 = t4p2_elochange
        t4p2.elo_change = t4p2.elo_change1+ t4p2.elo_change2+ t4p2.elo_change3+ t4p2.elo_change4+ t4p2.elo_change5
        
        t4p2.acts_ran += 1
        t4p2.total_points += team4player2
        t4p2.accum_competitor_elo += t4Comp #THIS WILL BE CALCULATED ABOVE, SO THIS LINE CAN BE DELETED

        t4p2.save()


        score_list = [team1player1, team1player2, team2player1, team2player2, team3player1, team3player2, team4player1, team4player2]

        for score in score_list:
            print("SCORE SD:")
            print(overall.score_sd)
            overall.sum_sq = overall.sum_sq + score * score
            overall.score_count += 1
            overall.total_score += score

        new_variance = (overall.sum_sq - (overall.total_score * overall.total_score)/overall.score_count)/overall.score_count
        overall.score_sd = math.sqrt(new_variance)
        overall.save()
        #return redirect('ranks:data2')
        
#UPDATE CHARACTER HANDICAPS


        counter = 0
        for score in score_list:
            index = int(counter/2) #finds the correct team
            print(character_combo_count_array[index])
            char_count = getattr(overall, character_combo_count_array[index])
            old_z = getattr(overall, character_combo_array[index])
            old_char_avg = 12 + old_z*overall.score_sd
            new_char_avg = (old_char_avg*char_count + (12*(score/exp_pts_unadj_array[counter])))/(char_count + 1)
            setattr(overall, character_combo_array[index], (new_char_avg - 12)/overall.score_sd)
            counter+=1
            setattr(overall, character_combo_count_array[index], getattr(overall, character_combo_count_array[index]) + 1)
        
        overall.save()
        
#RENDER
    return render(request, 'ranks/teamData.html', {})

#def enterData(request):

#    return render(request, "ranks/raceData.html", {'raceform':racesForm})

def listACTS(request):
    acts = ACT.objects.order_by('-act_id')
    acts_dict = {}
    for act_object in acts:
        acts_dict[act_object.act_id] = act_object
    return render(request, "", {'dict':acts_dict})

