# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=17)),
                ('top1', models.CharField(max_length=30)),
                ('top2', models.CharField(max_length=30)),
                ('top3', models.CharField(max_length=30)),
                ('top4', models.CharField(max_length=30)),
                ('top5', models.CharField(max_length=30)),
                ('top6', models.CharField(max_length=30)),
                ('top7', models.CharField(max_length=30)),
                ('top8', models.CharField(max_length=30)),
                ('top9', models.CharField(max_length=30)),
                ('top10', models.CharField(max_length=30)),
            ],
        ),
    ]
