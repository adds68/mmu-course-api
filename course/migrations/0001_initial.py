# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('credits', models.PositiveIntegerField()),
                ('duration', models.DurationField()),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('room', models.CharField(blank=True, max_length=100)),
                ('school', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ManyToManyField(to='course.Tutor'),
        ),
    ]
