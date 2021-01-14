from django.shortcuts import render
from .models import Player, PlayerEntry, Team, ACT

# Create your views here.

def home(request):
    #players = ["Eashan Panjwani","Zach Bell","Benner Mullin","Jackson Brodwolf","Matt Halper","Alex Hazel","Harris Klein","Kohl Terry","Alex Mellas","Noah Paige","Julian Ricci","Robbie Kramer","Ethan Roberts","Henry Rogers","Ryan Simon","Peter Netchvolodoff","Andrew Schanuel","Avery Friedman","Josh Greenfield","Will Spartin","Will Goldberg","Brady Sheaffer","Aman Patil","Zach Stern","Josh Josef","Nico Simon", "Sam Schoepke", "James Berthoud","Jonathan Nurko", "Spencer Gladstone","Kion Noori", "Max Marchetto", "Chuck Leonetti", "Matt Flower", "Connor Caz", "Caleb Hughes", "Lukas Steinbock","Brian Volk"]
    player_dict = {}
    players = Player.objects.order_by('-elo')
    for player_object in players:
        player_dict[player_object.name] = player_object
    return render(request, "ranks/home.html", {'dict': player_dict})
        

