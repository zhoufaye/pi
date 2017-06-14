# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yunwei', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=20)),
                ('command', models.CharField(max_length=300)),
                ('who', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='hostname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]