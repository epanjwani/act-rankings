from django.urls import path
from . import views

app_name = 'ranks'
urlpatterns = [
    path('', views.home, name='home'),
    path('data', views.enterTeamData, name='data1'),
]