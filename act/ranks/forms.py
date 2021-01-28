from django import forms
from .models import Player, ACT, Team, Race
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, MultiField

class actForm(forms.ModelForm):
    class Meta:
        model = ACT
        fields = ['name', 't1player1', 't1player2', 't1character_1', 't1character_2','t2player1', 't2player2', 't2character_1', 't2character_2', 't3player1', 't3player2', 't3character_1', 't3character_2','t4player1', 't4player2', 't4character_1', 't4character_2', 'oneteam1racer', 'onepoints1', 'oneteam2racer', 'onepoints2', 'oneteam3racer', 'onepoints3', 'oneteam4racer', 'onepoints4', 'twoteam1racer', 'twopoints1', 'twoteam2racer', 'twopoints2', 'twoteam3racer', 'twopoints3', 'twoteam4racer', 'twopoints4', 'threeteam1racer', 'threepoints1', 'threeteam2racer', 'threepoints2', 'threeteam3racer', 'threepoints3', 'threeteam4racer', 'threepoints4', 'fourteam1racer', 'fourpoints1', 'fourteam2racer', 'fourpoints2', 'fourteam3racer', 'fourpoints3', 'fourteam4racer', 'fourpoints4', 'fiveteam1racer', 'fivepoints1', 'fiveteam2racer', 'fivepoints2', 'fiveteam3racer', 'fivepoints3', 'fiveteam4racer', 'fivepoints4', 'sixteam1racer', 'sixpoints1', 'sixteam2racer', 'sixpoints2', 'sixteam3racer', 'sixpoints3', 'sixteam4racer', 'sixpoints4', 'seventeam1racer', 'sevenpoints1', 'seventeam2racer', 'sevenpoints2', 'seventeam3racer', 'sevenpoints3', 'seventeam4racer', 'sevenpoints4', 'eightteam1racer', 'eightpoints1', 'eightteam2racer', 'eightpoints2', 'eightteam3racer', 'eightpoints3', 'eightteam4racer', 'eightpoints4', 'nineteam1racer', 'ninepoints1', 'nineteam2racer', 'ninepoints2', 'nineteam3racer', 'ninepoints3', 'nineteam4racer', 'ninepoints4', 'tenteam1racer', 'tenpoints1', 'tenteam2racer', 'tenpoints2', 'tenteam3racer', 'tenpoints3', 'tenteam4racer', 'tenpoints4', 'eleventeam1racer', 'elevenpoints1', 'eleventeam2racer', 'elevenpoints2', 'eleventeam3racer', 'elevenpoints3', 'eleventeam4racer', 'elevenpoints4', 'twelveteam1racer', 'twelvepoints1', 'twelveteam2racer', 'twelvepoints2', 'twelveteam3racer', 'twelvepoints3', 'twelveteam4racer', 'twelvepoints4', 'thirteenteam1racer', 'thirteenpoints1', 'thirteenteam2racer', 'thirteenpoints2', 'thirteenteam3racer', 'thirteenpoints3', 'thirteenteam4racer', 'thirteenpoints4', 'fourteenteam1racer', 'fourteenpoints1', 'fourteenteam2racer', 'fourteenpoints2', 'fourteenteam3racer', 'fourteenpoints3', 'fourteenteam4racer', 'fourteenpoints4', 'fifteenteam1racer', 'fifteenpoints1', 'fifteenteam2racer', 'fifteenpoints2', 'fifteenteam3racer', 'fifteenpoints3', 'fifteenteam4racer', 'fifteenpoints4', 'sixteenteam1racer', 'sixteenpoints1', 'sixteenteam2racer', 'sixteenpoints2', 'sixteenteam3racer', 'sixteenpoints3', 'sixteenteam4racer', 'sixteenpoints4']
    def __init__(self, *args, **kwargs):
        super(actForm, self).__init__(*args, **kwargs)
        self.fields['t1player1'].label = 'Team 1 Player 1'
        self.fields['t1player2'].label = 'Team 1 Player 2'
        self.fields['t2player1'].label = 'Team 2 Player 1'
        self.fields['t2player2'].label = 'Team 2 Player 2'
        self.fields['t3player1'].label = 'Team 3 Player 1'
        self.fields['t3player2'].label = 'Team 3 Player 2'
        self.fields['t4player1'].label = 'Team 4 Player 1'
        self.fields['t4player2'].label = 'Team 4 Player 2'
        
        self.fields['t1character_1'].label = 'Team 1 Character 1'
        self.fields['t1character_2'].label = 'Team 1 Character 2'
        self.fields['t2character_1'].label = 'Team 2 Character 1'
        self.fields['t2character_2'].label = 'Team 2 Character 2'
        self.fields['t3character_1'].label = 'Team 3 Character 1'
        self.fields['t3character_2'].label = 'Team 3 Character 2'
        self.fields['t4character_1'].label = 'Team 4 Character 1'
        self.fields['t4character_2'].label = 'Team 4 Character 2'

        self.fields['oneteam1racer'].label = 'Luigi Circuit Team 1 Racer'
        self.fields['onepoints1'].label = 'Luigi Circuit Team 1 Points'
        self.fields['oneteam2racer'].label = 'Luigi Circuit Team 2 Racer'
        self.fields['onepoints2'].label = 'Luigi Circuit Team 2 Points'
        self.fields['oneteam3racer'].label = 'Luigi Circuit Team 3 Racer'
        self.fields['onepoints3'].label = 'Luigi Circuit Team 3 Points'
        self.fields['oneteam4racer'].label = 'Luigi Circuit Team 4 Racer'
        self.fields['onepoints4'].label = 'Luigi Circuit Team 4 Points'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            MultiField("Luigi Circuit",
                'oneteam1racer',
                'onepoints1',
                'oneteam2racer',
                'onepoints2',
                'oneteam3racer',
                'onepoints3',
                'oneteam4racer',
                'onepoints4'
            ),
        )
        #return super(actForm, self).__init__(*args, **kwargs)


#class racesForm(forms.Form):
    #fields = ['1team1racer', '1points1', '1team2racer', '1points2', '1team3racer', '1points3', '1team4racer', '1points4', '2team1racer', '2points1', '2team2racer', '2points2', '2team3racer', '2points3', '2team4racer', '2points4', '3team1racer', '3points1', '3team2racer', '3points2', '3team3racer', '3points3', '3team4racer', '3points4', '4team1racer', '4points1', '4team2racer', '4points2', '4team3racer', '4points3', '4team4racer', '4points4', '5team1racer', '5points1', '5team2racer', '5points2', '5team3racer', '5points3', '5team4racer', '5points4', '6team1racer', '6points1', '6team2racer', '6points2', '6team3racer', '6points3', '6team4racer', '6points4', '7team1racer', '7points1', '7team2racer', '7points2', '7team3racer', '7points3', '7team4racer', '7points4', '8team1racer', '8points1', '8team2racer', '8points2', '8team3racer', '8points3', '8team4racer', '8points4', '9team1racer', '9points1', '9team2racer', '9points2', '9team3racer', '9points3', '9team4racer', '9points4', '10team1racer', '10points1', '10team2racer', '10points2', '10team3racer', '10points3', '10team4racer', '10points4', 'eleventeam1racer', '11points1', '11team2racer', '11points2', '11team3racer', '11points3', '11team4racer', '11points4', '12team1racer', '12points1', '12team2racer', '12points2', '12team3racer', '12points3', '12team4racer', '12points4', 'thirteenteam1racer', 'thirteenpoints1', '13team2racer', '13points2', '13team3racer', '13points3', '13team4racer', '13points4', '14team1racer', '14points1', '14team2racer', '14points2', '14team3racer', '14points3', '14team4racer', '14points4', '15team1racer', '15points1', '15team2racer', '15points2', '15team3racer', '15points3', '15team4racer', '15points4', '16team1racer', '16points1', '16team2racer', '16points2', '16team3racer', '16points3', '16team4racer', '16points4']
    

