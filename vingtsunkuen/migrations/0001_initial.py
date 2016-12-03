# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, default='')),
                ('path', models.CharField(max_length=256, default='')),
                ('order', models.IntegerField()),
                ('category', models.CharField(max_length=50, default='')),
                ('category_order', models.IntegerField()),
            ],
        ),
    ]
