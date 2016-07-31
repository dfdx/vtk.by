# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vt', '0004_auto_20160601_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('slug', models.CharField(max_length=1024)),
                ('text', models.TextField()),
                ('lang', models.CharField(max_length=20)),
            ],
        ),
    ]
