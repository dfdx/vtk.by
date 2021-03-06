# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vt', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=2048)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
