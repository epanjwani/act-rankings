from django import forms
from .models import Player, ACT, Team, Race
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, MultiField, ButtonHolder, Submit, Field

class actForm(forms.ModelForm):
    class Meta:
        model = ACT
        fields = ['name', 't1player1', 't1player2', 't1character_1', 't1character_2','t2player1', 't2player2', 't2character_1', 't2character_2', 't3player1', 't3player2', 't3character_1', 't3character_2','t4player1', 't4player2', 't4character_1', 't4character_2', 'oneteam1racer', 'onepoints1', 'oneteam2racer', 'onepoints2', 'oneteam3racer', 'onepoints3', 'oneteam4racer', 'onepoints4', 'twoteam1racer', 'twopoints1', 'twoteam2racer', 'twopoints2', 'twoteam3racer', 'twopoints3', 'twoteam4racer', 'twopoints4', 'threeteam1racer', 'threepoints1', 'threeteam2racer', 'threepoints2', 'threeteam3racer', 'threepoints3', 'threeteam4racer', 'threepoints4', 'fourteam1racer', 'fourpoints1', 'fourteam2racer', 'fourpoints2', 'fourteam3racer', 'fourpoints3', 'fourteam4racer', 'fourpoints4', 'fiveteam1racer', 'fivepoints1', 'fiveteam2racer', 'fivepoints2', 'fiveteam3racer', 'fivepoints3', 'fiveteam4racer', 'fivepoints4', 'sixteam1racer', 'sixpoints1', 'sixteam2racer', 'sixpoints2', 'sixteam3racer', 'sixpoints3', 'sixteam4racer', 'sixpoints4', 'seventeam1racer', 'sevenpoints1', 'seventeam2racer', 'sevenpoints2', 'seventeam3racer', 'sevenpoints3', 'seventeam4racer', 'sevenpoints4', 'eightteam1racer', 'eightpoints1', 'eightteam2racer', 'eightpoints2', 'eightteam3racer', 'eightpoints3', 'eightteam4racer', 'eightpoints4', 'nineteam1racer', 'ninepoints1', 'nineteam2racer', 'ninepoints2', 'nineteam3racer', 'ninepoints3', 'nineteam4racer', 'ninepoints4', 'tenteam1racer', 'tenpoints1', 'tenteam2racer', 'tenpoints2', 'tenteam3racer', 'tenpoints3', 'tenteam4racer', 'tenpoints4', 'eleventeam1racer', 'elevenpoints1', 'eleventeam2racer', 'elevenpoints2', 'eleventeam3racer', 'elevenpoints3', 'eleventeam4racer', 'elevenpoints4', 'twelveteam1racer', 'twelvepoints1', 'twelveteam2racer', 'twelvepoints2', 'twelveteam3racer', 'twelvepoints3', 'twelveteam4racer', 'twelvepoints4', 'thirteenteam1racer', 'thirteenpoints1', 'thirteenteam2racer', 'thirteenpoints2', 'thirteenteam3racer', 'thirteenpoints3', 'thirteenteam4racer', 'thirteenpoints4', 'fourteenteam1racer', 'fourteenpoints1', 'fourteenteam2racer', 'fourteenpoints2', 'fourteenteam3racer', 'fourteenpoints3', 'fourteenteam4racer', 'fourteenpoints4', 'fifteenteam1racer', 'fifteenpoints1', 'fifteenteam2racer', 'fifteenpoints2', 'fifteenteam3racer', 'fifteenpoints3', 'fifteenteam4racer', 'fifteenpoints4', 'sixteenteam1racer', 'sixteenpoints1', 'sixteenteam2racer', 'sixteenpoints2', 'sixteenteam3racer', 'sixteenpoints3', 'sixteenteam4racer', 'sixteenpoints4']
    def __init__(self, *args, **kwargs):
        super(actForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
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

        self.fields['oneteam1racer'].label = 'Team 1 Racer'
        self.fields['onepoints1'].label = 'Team 1 Points'
        self.fields['oneteam2racer'].label = 'Team 2 Racer'
        self.fields['onepoints2'].label = 'Team 2 Points'
        self.fields['oneteam3racer'].label = 'Team 3 Racer'
        self.fields['onepoints3'].label = 'Team 3 Points'
        self.fields['oneteam4racer'].label = 'Team 4 Racer'
        self.fields['onepoints4'].label = 'Team 4 Points'

        self.fields['twoteam1racer'].label = 'Team 1 Racer'
        self.fields['twopoints1'].label = 'Team 1 Points'
        self.fields['twoteam2racer'].label = 'Team 2 Racer'
        self.fields['twopoints2'].label = 'Team 2 Points'
        self.fields['twoteam3racer'].label = 'Team 3 Racer'
        self.fields['twopoints3'].label = 'Team 3 Points'
        self.fields['twoteam4racer'].label = 'Team 4 Racer'
        self.fields['twopoints4'].label = 'Team 4 Points'

        self.fields['threeteam1racer'].label = 'Team 1 Racer'
        self.fields['threepoints1'].label = 'Team 1 Points'
        self.fields['threeteam2racer'].label = 'Team 2 Racer'
        self.fields['threepoints2'].label = 'Team 2 Points'
        self.fields['threeteam3racer'].label = 'Team 3 Racer'
        self.fields['threepoints3'].label = 'Team 3 Points'
        self.fields['threeteam4racer'].label = 'Team 4 Racer'
        self.fields['threepoints4'].label = 'Team 4 Points'

        self.fields['fourteam1racer'].label = 'Team 1 Racer'
        self.fields['fourpoints1'].label = 'Team 1 Points'
        self.fields['fourteam2racer'].label = 'Team 2 Racer'
        self.fields['fourpoints2'].label = 'Team 2 Points'
        self.fields['fourteam3racer'].label = 'Team 3 Racer'
        self.fields['fourpoints3'].label = 'Team 3 Points'
        self.fields['fourteam4racer'].label = 'Team 4 Racer'
        self.fields['fourpoints4'].label = 'Team 4 Points'

        self.fields['fiveteam1racer'].label = 'Team 1 Racer'
        self.fields['fivepoints1'].label = 'Team 1 Points'
        self.fields['fiveteam2racer'].label = 'Team 2 Racer'
        self.fields['fivepoints2'].label = 'Team 2 Points'
        self.fields['fiveteam3racer'].label = 'Team 3 Racer'
        self.fields['fivepoints3'].label = 'Team 3 Points'
        self.fields['fiveteam4racer'].label = 'Team 4 Racer'
        self.fields['fivepoints4'].label = 'Team 4 Points'

        self.fields['sixteam1racer'].label = 'Team 1 Racer'
        self.fields['sixpoints1'].label = 'Team 1 Points'
        self.fields['sixteam2racer'].label = 'Team 2 Racer'
        self.fields['sixpoints2'].label = 'Team 2 Points'
        self.fields['sixteam3racer'].label = 'Team 3 Racer'
        self.fields['sixpoints3'].label = 'Team 3 Points'
        self.fields['sixteam4racer'].label = 'Team 4 Racer'
        self.fields['sixpoints4'].label = 'Team 4 Points'

        self.fields['seventeam1racer'].label = 'Team 1 Racer'
        self.fields['sevenpoints1'].label = 'Team 1 Points'
        self.fields['seventeam2racer'].label = 'Team 2 Racer'
        self.fields['sevenpoints2'].label = 'Team 2 Points'
        self.fields['seventeam3racer'].label = 'Team 3 Racer'
        self.fields['sevenpoints3'].label = 'Team 3 Points'
        self.fields['seventeam4racer'].label = 'Team 4 Racer'
        self.fields['sevenpoints4'].label = 'Team 4 Points'

        self.fields['eightteam1racer'].label = 'Team 1 Racer'
        self.fields['eightpoints1'].label = 'Team 1 Points'
        self.fields['eightteam2racer'].label = 'Team 2 Racer'
        self.fields['eightpoints2'].label = 'Team 2 Points'
        self.fields['eightteam3racer'].label = 'Team 3 Racer'
        self.fields['eightpoints3'].label = 'Team 3 Points'
        self.fields['eightteam4racer'].label = 'Team 4 Racer'
        self.fields['eightpoints4'].label = 'Team 4 Points'

        self.fields['nineteam1racer'].label = 'Team 1 Racer'
        self.fields['ninepoints1'].label = 'Team 1 Points'
        self.fields['nineteam2racer'].label = 'Team 2 Racer'
        self.fields['ninepoints2'].label = 'Team 2 Points'
        self.fields['nineteam3racer'].label = 'Team 3 Racer'
        self.fields['ninepoints3'].label = 'Team 3 Points'
        self.fields['nineteam4racer'].label = 'Team 4 Racer'
        self.fields['ninepoints4'].label = 'Team 4 Points'

        self.fields['tenteam1racer'].label = 'Team 1 Racer'
        self.fields['tenpoints1'].label = 'Team 1 Points'
        self.fields['tenteam2racer'].label = 'Team 2 Racer'
        self.fields['tenpoints2'].label = 'Team 2 Points'
        self.fields['tenteam3racer'].label = 'Team 3 Racer'
        self.fields['tenpoints3'].label = 'Team 3 Points'
        self.fields['tenteam4racer'].label = 'Team 4 Racer'
        self.fields['tenpoints4'].label = 'Team 4 Points'

        self.fields['eleventeam1racer'].label = 'Team 1 Racer'
        self.fields['elevenpoints1'].label = 'Team 1 Points'
        self.fields['eleventeam2racer'].label = 'Team 2 Racer'
        self.fields['elevenpoints2'].label = 'Team 2 Points'
        self.fields['eleventeam3racer'].label = 'Team 3 Racer'
        self.fields['elevenpoints3'].label = 'Team 3 Points'
        self.fields['eleventeam4racer'].label = 'Team 4 Racer'
        self.fields['elevenpoints4'].label = 'Team 4 Points'

        self.fields['twelveteam1racer'].label = 'Team 1 Racer'
        self.fields['twelvepoints1'].label = 'Team 1 Points'
        self.fields['twelveteam2racer'].label = 'Team 2 Racer'
        self.fields['twelvepoints2'].label = 'Team 2 Points'
        self.fields['twelveteam3racer'].label = 'Team 3 Racer'
        self.fields['twelvepoints3'].label = 'Team 3 Points'
        self.fields['twelveteam4racer'].label = 'Team 4 Racer'
        self.fields['twelvepoints4'].label = 'Team 4 Points'

        self.fields['thirteenteam1racer'].label = 'Team 1 Racer'
        self.fields['thirteenpoints1'].label = 'Team 1 Points'
        self.fields['thirteenteam2racer'].label = 'Team 2 Racer'
        self.fields['thirteenpoints2'].label = 'Team 2 Points'
        self.fields['thirteenteam3racer'].label = 'Team 3 Racer'
        self.fields['thirteenpoints3'].label = 'Team 3 Points'
        self.fields['thirteenteam4racer'].label = 'Team 4 Racer'
        self.fields['thirteenpoints4'].label = 'Team 4 Points'

        self.fields['fourteenteam1racer'].label = 'Team 1 Racer'
        self.fields['fourteenpoints1'].label = 'Team 1 Points'
        self.fields['fourteenteam2racer'].label = 'Team 2 Racer'
        self.fields['fourteenpoints2'].label = 'Team 2 Points'
        self.fields['fourteenteam3racer'].label = 'Team 3 Racer'
        self.fields['fourteenpoints3'].label = 'Team 3 Points'
        self.fields['fourteenteam4racer'].label = 'Team 4 Racer'
        self.fields['fourteenpoints4'].label = 'Team 4 Points'

        self.fields['fifteenteam1racer'].label = 'Team 1 Racer'
        self.fields['fifteenpoints1'].label = 'Team 1 Points'
        self.fields['fifteenteam2racer'].label = 'Team 2 Racer'
        self.fields['fifteenpoints2'].label = 'Team 2 Points'
        self.fields['fifteenteam3racer'].label = 'Team 3 Racer'
        self.fields['fifteenpoints3'].label = 'Team 3 Points'
        self.fields['fifteenteam4racer'].label = 'Team 4 Racer'
        self.fields['fifteenpoints4'].label = 'Team 4 Points'

        self.fields['sixteenteam1racer'].label = 'Team 1 Racer'
        self.fields['sixteenpoints1'].label = 'Team 1 Points'
        self.fields['sixteenteam2racer'].label = 'Team 2 Racer'
        self.fields['sixteenpoints2'].label = 'Team 2 Points'
        self.fields['sixteenteam3racer'].label = 'Team 3 Racer'
        self.fields['sixteenpoints3'].label = 'Team 3 Points'
        self.fields['sixteenteam4racer'].label = 'Team 4 Racer'
        self.fields['sixteenpoints4'].label = 'Team 4 Points'

        self.helper.form_show_errors = False
        self.helper.error_text_inline = False

        
        self.helper.layout = Layout(
            Field('name'),
            MultiField("Team 1",
                't1player1',
                't1player2',
                't1character_1',
                't1character_2'
            ),
            MultiField("Team 2",
                't2player1',
                't2player2',
                't2character_1',
                't2character_2'
            ),
            MultiField("Team 3",
                't3player1',
                't3player2',
                't3character_1',
                't3character_2'
            ),
            MultiField("Team 4",
                't4player1',
                't4player2',
                't4character_1',
                't4character_2'
            ),
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
            MultiField("Peach Beach",
                'twoteam1racer',
                'twopoints1',
                'twoteam2racer',
                'twopoints2',
                'twoteam3racer',
                'twopoints3',
                'twoteam4racer',
                'twopoints4'
            ),
            MultiField("Baby Park",
                'threeteam1racer',
                'threepoints1',
                'threeteam2racer',
                'threepoints2',
                'threeteam3racer',
                'threepoints3',
                'threeteam4racer',
                'threepoints4'
            ),
            MultiField("Dry Dry Desert",
                'fourteam1racer',
                'fourpoints1',
                'fourteam2racer',
                'fourpoints2',
                'fourteam3racer',
                'fourpoints3',
                'fourteam4racer',
                'fourpoints4'
            ),
            MultiField("Mushroom Bridge",
                'fiveteam1racer',
                'fivepoints1',
                'fiveteam2racer',
                'fivepoints2',
                'fiveteam3racer',
                'fivepoints3',
                'fiveteam4racer',
                'fivepoints4'
            ),
            MultiField("Mario Circuit",
                'sixteam1racer',
                'sixpoints1',
                'sixteam2racer',
                'sixpoints2',
                'sixteam3racer',
                'sixpoints3',
                'sixteam4racer',
                'sixpoints4'
            ),
            MultiField("Daisy Cruiser",
                'seventeam1racer',
                'sevenpoints1',
                'seventeam2racer',
                'sevenpoints2',
                'seventeam3racer',
                'sevenpoints3',
                'seventeam4racer',
                'sevenpoints4'
            ),
            MultiField("Waluigi Stadium",
                'eightteam1racer',
                'eightpoints1',
                'eightteam2racer',
                'eightpoints2',
                'eightteam3racer',
                'eightpoints3',
                'eightteam4racer',
                'eightpoints4'
            ),
            MultiField("Sherbet Land",
                'nineteam1racer',
                'ninepoints1',
                'nineteam2racer',
                'ninepoints2',
                'nineteam3racer',
                'ninepoints3',
                'nineteam4racer',
                'ninepoints4'
            ),
            MultiField("Mushroom City",
                'tenteam1racer',
                'tenpoints1',
                'tenteam2racer',
                'tenpoints2',
                'tenteam3racer',
                'tenpoints3',
                'tenteam4racer',
                'tenpoints4'
            ),
            MultiField("Yoshi Circuit",
                'eleventeam1racer',
                'elevenpoints1',
                'eleventeam2racer',
                'elevenpoints2',
                'eleventeam3racer',
                'elevenpoints3',
                'eleventeam4racer',
                'elevenpoints4'
            ),
            MultiField("DK Mountain",
                'twelveteam1racer',
                'twelvepoints1',
                'twelveteam2racer',
                'twelvepoints2',
                'twelveteam3racer',
                'twelvepoints3',
                'twelveteam4racer',
                'twelvepoints4'
            ),
            MultiField("Wario Colosseum",
                'thirteenteam1racer',
                'thirteenpoints1',
                'thirteenteam2racer',
                'thirteenpoints2',
                'thirteenteam3racer',
                'thirteenpoints3',
                'thirteenteam4racer',
                'thirteenpoints4'
            ),
            MultiField("Dino Dino Jungle",
                'fourteenteam1racer',
                'fourteenpoints1',
                'fourteenteam2racer',
                'fourteenpoints2',
                'fourteenteam3racer',
                'fourteenpoints3',
                'fourteenteam4racer',
                'fourteenpoints4'
            ),
            MultiField("Bowser Castle",
                'fifteenteam1racer',
                'fifteenpoints1',
                'fifteenteam2racer',
                'fifteenpoints2',
                'fifteenteam3racer',
                'fifteenpoints3',
                'fifteenteam4racer',
                'fifteenpoints4'
            ),
            MultiField("Rainbow Road",
                'sixteenteam1racer',
                'sixteenpoints1',
                'sixteenteam2racer',
                'sixteenpoints2',
                'sixteenteam3racer',
                'sixteenpoints3',
                'sixteenteam4racer',
                'sixteenpoints4'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
        
        #return super(actForm, self).__init__(*args, **kwargs)


#class racesForm(forms.Form):
    #fields = ['1team1racer', '1points1', '1team2racer', '1points2', '1team3racer', '1points3', '1team4racer', '1points4', '2team1racer', '2points1', '2team2racer', '2points2', '2team3racer', '2points3', '2team4racer', '2points4', '3team1racer', '3points1', '3team2racer', '3points2', '3team3racer', '3points3', '3team4racer', '3points4', '4team1racer', '4points1', '4team2racer', '4points2', '4team3racer', '4points3', '4team4racer', '4points4', '5team1racer', '5points1', '5team2racer', '5points2', '5team3racer', '5points3', '5team4racer', '5points4', '6team1racer', '6points1', '6team2racer', '6points2', '6team3racer', '6points3', '6team4racer', '6points4', '7team1racer', '7points1', '7team2racer', '7points2', '7team3racer', '7points3', '7team4racer', '7points4', '8team1racer', '8points1', '8team2racer', '8points2', '8team3racer', '8points3', '8team4racer', '8points4', '9team1racer', '9points1', '9team2racer', '9points2', '9team3racer', '9points3', '9team4racer', '9points4', '10team1racer', '10points1', '10team2racer', '10points2', '10team3racer', '10points3', '10team4racer', '10points4', 'eleventeam1racer', '11points1', '11team2racer', '11points2', '11team3racer', '11points3', '11team4racer', '11points4', '12team1racer', '12points1', '12team2racer', '12points2', '12team3racer', '12points3', '12team4racer', '12points4', 'thirteenteam1racer', 'thirteenpoints1', '13team2racer', '13points2', '13team3racer', '13points3', '13team4racer', '13points4', '14team1racer', '14points1', '14team2racer', '14points2', '14team3racer', '14points3', '14team4racer', '14points4', '15team1racer', '15points1', '15team2racer', '15points2', '15team3racer', '15points3', '15team4racer', '15points4', '16team1racer', '16points1', '16team2racer', '16points2', '16team3racer', '16points3', '16team4racer', '16points4']
    

