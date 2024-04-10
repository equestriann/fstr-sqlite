# Generated by Django 5.0.4 on 2024-04-10 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True)),
                ('longtitude', models.FloatField(blank=True)),
                ('height', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('---', '---'), ('n/c', 'н/к'), ('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='---', max_length=3)),
                ('spring', models.CharField(choices=[('---', '---'), ('n/c', 'н/к'), ('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='---', max_length=3)),
                ('summer', models.CharField(choices=[('---', '---'), ('n/c', 'н/к'), ('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='---', max_length=3)),
                ('autumn', models.CharField(choices=[('---', '---'), ('n/c', 'н/к'), ('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='---', max_length=3)),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровени сложности',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('otc', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'модерация'), ('accepted', 'принято'), ('rejected', 'отказано')], default='new', max_length=9)),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(blank=True, max_length=255)),
                ('connect', models.CharField(max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('coord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('level', models.OneToOneField(default='---', on_delete=django.db.models.deletion.CASCADE, to='pereval.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.users')),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.URLField(blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('rel_pass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.pass')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
