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
            infoDict['t1player1'] = act.t1player1.name
            infoDict['t1player2'] = act.t1player2.name
            infoDict['t1character_1'] = act.t1character_1
            infoDict['t1character_2'] = act.t1character_2
            infoDict['t2player1'] = act.t2player1.name
            infoDict['t2player2'] = act.t2player2.name
            infoDict['t2character_1'] = act.t2character_1
            infoDict['t2character_2'] = act.t2character_2
            infoDict['t3player1'] = act.t3player1.name
            infoDict['t3player2'] = act.t3player2.name
            infoDict['t3character_1'] = act.t3character_1
            infoDict['t3character_2'] = act.t3character_2
            infoDict['t4player1'] = act.t4player1.name
            infoDict['t4player2'] = act.t4player2.name
            infoDict['t4character_1'] = act.t4character_1
            infoDict['t4character_2'] = act.t4character_2
            request.session["currentACT"] = infoDict
            #return redirect('ranks:data2')
    return render(request, 'ranks/teamData.html', {'actform':form})

#def enterData(request):
#    return render(request, "ranks/raceData.html", {'raceform':racesForm})
