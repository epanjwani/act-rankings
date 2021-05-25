# Generated by Django 3.1.5 on 2021-05-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranks', '0005_auto_20210319_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='elo_change1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='elo_change2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='elo_change3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='elo_change4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='elo_change5',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(choices=[('Eashan Panjwani', 'EP'), ('Zach Bell', 'ZB'), ('Benner Mullin', 'BM'), ('Jackson Brodwolf', 'JB'), ('Matt Halper', 'MH'), ('Alex Hazel', 'AH'), ('Harris Klein', 'HK'), ('Kohl Terry', 'KT'), ('Alex Mellas', 'AM'), ('Noah Paige', 'NP'), ('Julian Ricci', 'JR'), ('Robbie Kramer', 'RK'), ('Ethan Roberts', 'ER'), ('Henry Rogers', 'HR'), ('Ryan Simon', 'RS'), ('Peter Netch', 'PN'), ('Andrew Schanny', 'AS'), ('Avery Friedman', 'AF'), ('Josh Greenfield', 'JG'), ('Will Spartin', 'WS'), ('Will Goldberg', 'WG'), ('Brady Sheaffer', 'BS'), ('Aman Patil', 'AP'), ('Zach Stern', 'ZS'), ('Josh Josef', 'JJ'), ('Nico Simon', 'NS'), ('Sam Schoepke', 'SS'), ('James Berthoud', 'JBe'), ('Jonathan Nurko', 'JN'), ('Spencer Gladstone', 'SG'), ('Kion Noori', 'KN'), ('Max Marchetto', 'MM'), ('Chuck Leonetti', 'CL'), ('Matt Flower', 'MF'), ('Connor Caz', 'CC'), ('Caleb Hughes', 'CH'), ('Lukas Steinbock', 'LS'), ('Brian Volk', 'BV'), ('Nitan Shalon', 'NSh'), ('Mat Zlotnick', 'MZ'), ('Gavin Morse', 'GM')], max_length=50),
        ),
        migrations.AlterField(
            model_name='playerentry',
            name='name',
            field=models.CharField(choices=[('Eashan Panjwani', 'EP'), ('Zach Bell', 'ZB'), ('Benner Mullin', 'BM'), ('Jackson Brodwolf', 'JB'), ('Matt Halper', 'MH'), ('Alex Hazel', 'AH'), ('Harris Klein', 'HK'), ('Kohl Terry', 'KT'), ('Alex Mellas', 'AM'), ('Noah Paige', 'NP'), ('Julian Ricci', 'JR'), ('Robbie Kramer', 'RK'), ('Ethan Roberts', 'ER'), ('Henry Rogers', 'HR'), ('Ryan Simon', 'RS'), ('Peter Netch', 'PN'), ('Andrew Schanny', 'AS'), ('Avery Friedman', 'AF'), ('Josh Greenfield', 'JG'), ('Will Spartin', 'WS'), ('Will Goldberg', 'WG'), ('Brady Sheaffer', 'BS'), ('Aman Patil', 'AP'), ('Zach Stern', 'ZS'), ('Josh Josef', 'JJ'), ('Nico Simon', 'NS'), ('Sam Schoepke', 'SS'), ('James Berthoud', 'TJ'), ('Jonathan Nurko', 'JN'), ('Spencer Gladstone', 'SG'), ('Kion Noori', 'KN'), ('Max Marchetto', 'MM'), ('Chuck Leonetti', 'CL'), ('Matt Flower', 'MF'), ('Connor Caz', 'CC'), ('Caleb Hughes', 'CH'), ('Lukas Steinbock', 'LS'), ('Brian Volk', 'BV')], max_length=50),
        ),
    ]
