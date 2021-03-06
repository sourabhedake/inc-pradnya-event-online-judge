# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_no', models.IntegerField(blank=True, default=-1, null=True)),
                ('questionid', models.CharField(blank=True, default='def', max_length=30, null=True)),
                ('score_obtained', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, default='', max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pradnya.user'),
        ),
    ]
