# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-09-27 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url', models.URLField()),
                ('registration_link', models.URLField(blank=True, null=True)),
                ('short_description', models.CharField(max_length=500)),
                ('long_description', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='tags',
            field=models.ManyToManyField(related_name='events', to='calendar_event_app.Tag'),
        ),
    ]
