from django.shortcuts import render, redirect
from .models import Player, PlayerEntry, Team, ACT
from .forms import actForm
import openpyxl

# Create your views here.

def home(request):
    #players = ["Eashan Panjwani","Zach Bell","Benner Mullin","Jackson Brodwolf","Matt Halper","Alex Hazel","Harris Klein","Kohl Terry","Alex Mellas","Noah Paige","Julian Ricci","Robbie Kramer","Ethan Roberts","Henry Rogers","Ryan Simon","Peter Netchvolodoff","Andrew Schanuel","Avery Friedman","Josh Greenfield","Will Spartin","Will Goldberg","Brady Sheaffer","Aman Patil","Zach Stern","Josh Josef","Nico Simon", "Sam Schoepke", "James Berthoud","Jonathan Nurko", "Spencer Gladstone","Kion Noori", "Max Marchetto", "Chuck Leonetti", "Matt Flower", "Connor Caz", "Caleb Hughes", "Lukas Steinbock","Brian Volk"]
    player_dict = {}
    players = Player.objects.order_by('-elo')
    for player_object in players:
        player_dict[player_object.name] = player_object
    return render(request, "ranks/home.html", {'dict': player_dict})


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
        

def enterTeamData(request):
    """ print("yay")
    print("yay!")
    form = actForm(request.POST)
    form.as_table()
    if form.is_valid():
        print("yay2!")
        act = form.save(commit=False) """
    if "GET" == request.method:
        return render(request, 'ranks/teamData.html', {})
    else:
        print("not lul")
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

        player_dict = {
            "EP" : "Eashan Panjwani",
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
            "GM" : "Gavin Morse",
        }

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
                if rowCount != 4 and rowCount != 5:
                    if cellCount == 3 and cell.value != None:
                        team1player1 += int(cell.value)
                    if cellCount == 4 and cell.value != None:
                        team1player2 += int(cell.value)
                    if cellCount == 5 and cell.value != None:
                        team2player1 += int(cell.value)
                    if cellCount == 6 and cell.value != None:
                        team2player2 += int(cell.value)
                    if cellCount == 7 and cell.value != None:
                        team3player1 += int(cell.value)
                    if cellCount == 8 and cell.value != None:
                        team3player2 += int(cell.value)
                    if cellCount == 9 and cell.value != None:
                        team4player1 += int(cell.value)
                    if cellCount == 10 and cell.value != None:
                        team4player2 += int(cell.value)
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
        """
        infoDict = {}
        infoDict['name'] = act.name

        teamDict = {}
        teamDict['t1player1'] = act.t1player1.name
        teamDict['t1player2'] = act.t1player2.name
        teamDict['t1character_1'] = act.t1character_1
        teamDict['t1character_2'] = act.t1character_2
        teamDict['t2player1'] = act.t2player1.name
        teamDict['t2player2'] = act.t2player2.name
        teamDict['t2character_1'] = act.t2character_1
        teamDict['t2character_2'] = act.t2character_2
        teamDict['t3player1'] = act.t3player1.name
        teamDict['t3player2'] = act.t3player2.name
        teamDict['t3character_1'] = act.t3character_1
        teamDict['t3character_2'] = act.t3character_2
        teamDict['t4player1'] = act.t4player1.name
        teamDict['t4player2'] = act.t4player2.name
        teamDict['t4character_1'] = act.t4character_1
        teamDict['t4character_2'] = act.t4character_2
        infoDict["teaminfo"] = teamDict

        """

        t1p1 = Player.objects.get(name=team1player1name)
        t1p2 = Player.objects.get(name=team1player2name)
        t2p1 = Player.objects.get(name=team2player1name)
        t2p2 = Player.objects.get(name=team2player2name)
        t3p1 = Player.objects.get(name=team3player1name)
        t3p2 = Player.objects.get(name=team3player2name)
        t4p1 = Player.objects.get(name=team4player1name)
        t4p2 = Player.objects.get(name=team4player2name)

        t1_elo = (t1p1.elo + t1p2.elo)/2
        t2_elo = (t2p1.elo + t2p2.elo)/2
        t3_elo = (t3p1.elo + t3p2.elo)/2
        t4_elo = (t4p1.elo + t4p2.elo)/2
        t1p1.save()

        t1_points = team1player1 + team1player2
        t2_points = team2player1 + team2player2
        t3_points = team3player1 + team3player2
        t4_points = team3player1 + team4player2

        t1_elochange = 0
        t2_elochange = 0
        t3_elochange = 0
        t4_elochange = 0

        """  """
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
        
        t1p1.elo += t1_elochange
        t1p1.elo_change = t1_elochange
        t1p1.acts_ran += 1
        t1p1.total_points += team1player1
        t1p1.save()

        t1p2.elo += t1_elochange
        t1p2.elo_change = t1_elochange
        t1p2.acts_ran += 1
        t1p2.total_points += team1player2
        t1p2.save()

        t2p1.elo += t2_elochange
        t2p1.elo_change = t2_elochange
        t2p1.acts_ran += 1
        t2p1.total_points += team2player1
        t2p1.save()

        t2p2.elo += t2_elochange
        t2p2.elo_change = t2_elochange
        t2p2.acts_ran += 1
        t2p2.total_points += team2player2
        t2p2.save()

        t3p1.elo += t3_elochange
        t3p1.elo_change = t3_elochange
        t3p1.acts_ran += 1
        t3p1.total_points += team3player1
        t3p1.save()

        t3p2.elo += t3_elochange
        t3p2.elo_change = t3_elochange
        t3p2.acts_ran += 1
        t3p2.total_points += team3player2
        t3p2.save()

        t4p1.elo += t4_elochange
        t4p1.elo_change = t4_elochange
        t4p1.acts_ran += 1
        t4p1.total_points += team4player1
        t4p1.save()

        t4p2.elo += t4_elochange
        t4p2.elo_change = t4_elochange
        t4p2.acts_ran += 1
        t4p2.total_points += team4player2
        t4p2.save()

        

        """
        LCDict = {}            
        LCDict['oneteam1racer'] = act.oneteam1racer
        LCDict['onepoints1'] = act.onepoints1
        LCDict['oneteam2racer'] = act.oneteam2racer
        LCDict['onepoints2'] = act.onepoints2
        LCDict['oneteam3racer'] = act.oneteam3racer
        LCDict['onepoints3'] = act.onepoints3
        LCDict['oneteam4racer'] = act.oneteam4racer
        LCDict['onepoints4'] = act.onepoints4
        infoDict["LCinfo"] = LCDict

        PBDict = {}            
        PBDict['twoteam1racer'] = act.twoteam1racer
        PBDict['twopoints1'] = act.twopoints1
        PBDict['twoteam2racer'] = act.twoteam2racer
        PBDict['twopoints2'] = act.twopoints2
        PBDict['twoteam3racer'] = act.twoteam3racer
        PBDict['twopoints3'] = act.twopoints3
        PBDict['twoteam4racer'] = act.twoteam4racer
        PBDict['twopoints4'] = act.twopoints4
        infoDict["PBinfo"] = PBDict

        BPDict = {}            
        BPDict['threeteam1racer'] = act.threeteam1racer
        BPDict['threepoints1'] = act.threepoints1
        BPDict['threeteam2racer'] = act.threeteam2racer
        BPDict['threepoints2'] = act.threepoints2
        BPDict['threeteam3racer'] = act.threeteam3racer
        BPDict['threepoints3'] = act.threepoints3
        BPDict['threeteam4racer'] = act.threeteam4racer
        BPDict['threepoints4'] = act.threepoints4
        infoDict["BPinfo"] = BPDict

        DDDDict = {}            
        DDDDict['fourteam1racer'] = act.fourteam1racer
        DDDDict['fourpoints1'] = act.fourpoints1
        DDDDict['fourteam2racer'] = act.fourteam2racer
        DDDDict['fourpoints2'] = act.fourpoints2
        DDDDict['fourteam3racer'] = act.fourteam3racer
        DDDDict['fourpoints3'] = act.fourpoints3
        DDDDict['fourteam4racer'] = act.fourteam4racer
        DDDDict['fourpoints4'] = act.fourpoints4
        infoDict["DDDinfo"] = DDDDict

        MBDict = {}            
        MBDict['fiveteam1racer'] = act.fiveteam1racer
        MBDict['fivepoints1'] = act.fivepoints1
        MBDict['fiveteam2racer'] = act.fiveteam2racer
        MBDict['fivepoints2'] = act.fivepoints2
        MBDict['fiveteam3racer'] = act.fiveteam3racer
        MBDict['fivepoints3'] = act.fivepoints3
        MBDict['fiveteam4racer'] = act.fiveteam4racer
        MBDict['fivepoints4'] = act.fivepoints4
        infoDict["MBinfo"] = MBDict

        MaCDict = {}            
        MaCDict['sixteam1racer'] = act.sixteam1racer
        MaCDict['sixpoints1'] = act.sixpoints1
        MaCDict['sixteam2racer'] = act.sixteam2racer
        MaCDict['sixpoints2'] = act.sixpoints2
        MaCDict['sixteam3racer'] = act.sixteam3racer
        MaCDict['sixpoints3'] = act.sixpoints3
        MaCDict['sixteam4racer'] = act.sixteam4racer
        MaCDict['sixpoints4'] = act.sixpoints4
        infoDict["MaCinfo"] = MaCDict

        DCDict = {}            
        DCDict['seventeam1racer'] = act.seventeam1racer
        DCDict['sevenpoints1'] = act.sevenpoints1
        DCDict['seventeam2racer'] = act.seventeam2racer
        DCDict['sevenpoints2'] = act.sevenpoints2
        DCDict['seventeam3racer'] = act.seventeam3racer
        DCDict['sevenpoints3'] = act.sevenpoints3
        DCDict['seventeam4racer'] = act.seventeam4racer
        DCDict['sevenpoints4'] = act.sevenpoints4
        infoDict["DCinfo"] = DCDict

        WSDict = {}            
        WSDict['eightteam1racer'] = act.eightteam1racer
        WSDict['eightpoints1'] = act.eightpoints1
        WSDict['eightteam2racer'] = act.eightteam2racer
        WSDict['eightpoints2'] = act.eightpoints2
        WSDict['eightteam3racer'] = act.eightteam3racer
        WSDict['eightpoints3'] = act.eightpoints3
        WSDict['eightteam4racer'] = act.eightteam4racer
        WSDict['eightpoints4'] = act.eightpoints4
        infoDict["WSinfo"] = WSDict

        SLDict = {}            
        SLDict['nineteam1racer'] = act.nineteam1racer
        SLDict['ninepoints1'] = act.ninepoints1
        SLDict['nineteam2racer'] = act.nineteam2racer
        SLDict['ninepoints2'] = act.ninepoints2
        SLDict['nineteam3racer'] = act.nineteam3racer
        SLDict['ninepoints3'] = act.ninepoints3
        SLDict['nineteam4racer'] = act.nineteam4racer
        SLDict['ninepoints4'] = act.ninepoints4
        infoDict["SLinfo"] = SLDict

        MuCDict = {}            
        MuCDict['tenteam1racer'] = act.tenteam1racer
        MuCDict['tenpoints1'] = act.tenpoints1
        MuCDict['tenteam2racer'] = act.tenteam2racer
        MuCDict['tenpoints2'] = act.tenpoints2
        MuCDict['tenteam3racer'] = act.tenteam3racer
        MuCDict['tenpoints3'] = act.tenpoints3
        MuCDict['tenteam4racer'] = act.tenteam4racer
        MuCDict['tenpoints4'] = act.tenpoints4
        infoDict["MuCinfo"] = MuCDict

        YCDict = {}            
        YCDict['eleventeam1racer'] = act.eleventeam1racer
        YCDict['elevenpoints1'] = act.elevenpoints1
        YCDict['eleventeam2racer'] = act.eleventeam2racer
        YCDict['elevenpoints2'] = act.elevenpoints2
        YCDict['eleventeam3racer'] = act.eleventeam3racer
        YCDict['elevenpoints3'] = act.elevenpoints3
        YCDict['eleventeam4racer'] = act.eleventeam4racer
        YCDict['elevenpoints4'] = act.elevenpoints4
        infoDict["YCinfo"] = YCDict

        DKDict = {}            
        DKDict['twelveteam1racer'] = act.twelveteam1racer
        DKDict['twelvepoints1'] = act.twelvepoints1
        DKDict['twelveteam2racer'] = act.twelveteam2racer
        DKDict['twelvepoints2'] = act.twelvepoints2
        DKDict['twelveteam3racer'] = act.twelveteam3racer
        DKDict['twelvepoints3'] = act.twelvepoints3
        DKDict['twelveteam4racer'] = act.twelveteam4racer
        DKDict['twelvepoints4'] = act.twelvepoints4
        infoDict["DKinfo"] = DKDict

        WCDict = {}            
        WCDict['thirteenteam1racer'] = act.thirteenteam1racer
        WCDict['thirteenpoints1'] = act.thirteenpoints1
        WCDict['thirteenteam2racer'] = act.thirteenteam2racer
        WCDict['thirteenpoints2'] = act.thirteenpoints2
        WCDict['thirteenteam3racer'] = act.thirteenteam3racer
        WCDict['thirteenpoints3'] = act.thirteenpoints3
        WCDict['thirteenteam4racer'] = act.thirteenteam4racer
        WCDict['thirteenpoints4'] = act.thirteenpoints4
        infoDict["WCinfo"] = WCDict

        DDJDict = {}            
        DDJDict['fourteenteam1racer'] = act.fourteenteam1racer
        DDJDict['fourteenpoints1'] = act.fourteenpoints1
        DDJDict['fourteenteam2racer'] = act.fourteenteam2racer
        DDJDict['fourteenpoints2'] = act.fourteenpoints2
        DDJDict['fourteenteam3racer'] = act.fourteenteam3racer
        DDJDict['fourteenpoints3'] = act.fourteenpoints3
        DDJDict['fourteenteam4racer'] = act.fourteenteam4racer
        DDJDict['fourteenpoints4'] = act.fourteenpoints4
        infoDict["DDJinfo"] = DDJDict

        BCDict = {}            
        BCDict['fifteenteam1racer'] = act.fifteenteam1racer
        BCDict['fifteenpoints1'] = act.fifteenpoints1
        BCDict['fifteenteam2racer'] = act.fifteenteam2racer
        BCDict['fifteenpoints2'] = act.fifteenpoints2
        BCDict['fifteenteam3racer'] = act.fifteenteam3racer
        BCDict['fifteenpoints3'] = act.fifteenpoints3
        BCDict['fifteenteam4racer'] = act.fifteenteam4racer
        BCDict['fifteenpoints4'] = act.fifteenpoints4
        infoDict["BCinfo"] = BCDict

        RRDict = {}            
        RRDict['sixteenteam1racer'] = act.sixteenteam1racer
        RRDict['sixteenpoints1'] = act.sixteenpoints1
        RRDict['sixteenteam2racer'] = act.sixteenteam2racer
        RRDict['sixteenpoints2'] = act.sixteenpoints2
        RRDict['sixteenteam3racer'] = act.sixteenteam3racer
        RRDict['sixteenpoints3'] = act.sixteenpoints3
        RRDict['sixteenteam4racer'] = act.sixteenteam4racer
        RRDict['sixteenpoints4'] = act.sixteenpoints4
        infoDict["RRinfo"] = RRDict

        request.session["currentACT"] = infoDict
        """


            #return redirect('ranks:data2')
    return render(request, 'ranks/teamData.html', {})


#def enterData(request):
#    return render(request, "ranks/raceData.html", {'raceform':racesForm})
