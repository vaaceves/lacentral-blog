# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20180427_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('course', models.BooleanField(default=False)),
                ('workshop', models.BooleanField(default=False)),
                ('starts', models.DateTimeField()),
                ('ends', models.DateTimeField()),
                ('place', models.CharField(max_length=250)),
                ('google_maps', models.CharField(max_length=140)),
                ('summary', models.TextField(null=True)),
                ('body', models.TextField()),
                ('price', models.FloatField()),
                ('free', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField()),
                ('HomePage', models.BooleanField()),
                ('img_cover', models.ImageField(null=True, upload_to='course-workshop-img-covers/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Category')),
                ('tags', models.ManyToManyField(to='posts.Tag')),
            ],
            options={
                'verbose_name': 'Course & Workshop',
                'verbose_name_plural': 'Courses & Workshops',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('starts', models.DateTimeField()),
                ('ends', models.DateTimeField()),
                ('place', models.CharField(max_length=250)),
                ('google_maps', models.CharField(max_length=140)),
                ('summary', models.TextField(null=True)),
                ('body', models.TextField()),
                ('price', models.FloatField()),
                ('free', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField()),
                ('HomePage', models.BooleanField()),
                ('img_cover', models.ImageField(null=True, upload_to='event-img-covers/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Category')),
                ('tags', models.ManyToManyField(to='posts.Tag')),
            ],
        ),
    ]