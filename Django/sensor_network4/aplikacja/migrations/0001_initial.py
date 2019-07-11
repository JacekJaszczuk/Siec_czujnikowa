# Generated by Django 2.2.1 on 2019-07-11 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miejsca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kontynent', models.CharField(max_length=30)),
                ('kraj', models.CharField(max_length=30)),
                ('obszar', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pacjent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.TextField(max_length=30)),
                ('data_urodzenia', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pomiar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('typ_pomiaru', models.CharField(max_length=30)),
                ('wartosc', models.FloatField()),
                ('miejsce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.Miejsca')),
                ('pacjent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.Pacjent')),
            ],
        ),
    ]
