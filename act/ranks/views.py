from django.shortcuts import render, redirect
from .models import Player, PlayerEntry, Team, ACT
from .forms import actForm

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
    if request.method == "GET":
        form = actForm(request.GET)
        form.as_table()
        if form.is_valid():
            act = form.save(commit=False)
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
            #return redirect('ranks:data2')
    return render(request, 'ranks/teamData.html', {'actform':form})

#def enterData(request):
#    return render(request, "ranks/raceData.html", {'raceform':racesForm})
