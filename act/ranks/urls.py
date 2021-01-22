from django.urls import path
from . import views

app_name = 'ranks'
urlpatterns = [
    path('', views.home, name='home'),
    path('player', views.player, name='player'),
    path('race', views.race, name='race'),
    path('data', views.enterTeamData, name='data1'),
    path('data2', views.enterData, name='data2')
]