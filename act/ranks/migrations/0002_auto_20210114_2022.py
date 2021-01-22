# Generated by Django 3.0.5 on 2021-01-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Luigi Circuit', 'Luigi Circuit'), ('Peach Beach', 'Peach Beach'), ('Baby Park', 'Baby Park'), ('Dry Dry Desert', 'Dry Dry Desert'), ('Mushroom Bridge', 'Mushroom Bridge'), ('Mario Circuit', 'Mario Circuit'), ('Daisy Cruiser', 'Daisy Cruiser'), ('Waluigi Stadium', 'Waluigi Stadium'), ('Sherbet Land', 'Sherbet Land'), ('Mushroom City', 'Mushroom City'), ('Yoshi Circuit', 'Yoshi Circuit'), ('DK Mountain', 'DK Mountain'), ('Wario Colloseum', 'Wario Colloseum'), ('Dino Dino Jungle', 'Dino Dino Jungle'), ('Bowser Castle', 'Bowser Castle'), ('Rainbow Road', 'Rainbow Road')], max_length=50)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='accum_competitor_elo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='acts_ran',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='elo_change',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='league',
            field=models.CharField(choices=[('A-League', 'A-League'), ('B-League', 'B-League'), ('C-League', 'C-League'), ('N/A', 'N/A')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]