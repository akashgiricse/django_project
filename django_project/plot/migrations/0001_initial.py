# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-03 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gata_number', models.CharField(default=None, max_length=50, verbose_name='गाटा संख्या')),
                ('area', models.FloatField(default=None, verbose_name='क्षेत्रफल (हैक्\u200dटेयर)')),
                ('shreni_desc', models.TextField()),
                ('distance_road', models.FloatField(default=None, verbose_name='सड़क से दूरी (कि.मी.)')),
                ('connectivity', models.BooleanField(verbose_name='कनेक्टिविटी')),
                ('allotted', models.BooleanField(default=False, verbose_name='आवंटित')),
                ('latitude_coordinate', models.CharField(default=None, max_length=15, verbose_name='अक्षांश निर्देशांक')),
                ('longitude_coordinate', models.CharField(default=None, max_length=15, verbose_name='देशांतर निर्देशांक')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shreni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shreni', models.CharField(max_length=10, verbose_name='श्रेणी')),
                ('shreni_description', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, verbose_name='गांव का नाम')),
                ('code', models.IntegerField(default=None, verbose_name='गांव कोड')),
            ],
        ),
        migrations.AddField(
            model_name='plot',
            name='shreni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plot.Shreni'),
        ),
        migrations.AddField(
            model_name='plot',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plot.Village'),
        ),
    ]
