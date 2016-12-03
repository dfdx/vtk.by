# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vingtsunkuen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=256, default='')),
                ('subpath', models.CharField(max_length=256, default='')),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='photoalbum',
            old_name='path',
            new_name='subpath',
        ),
        migrations.RemoveField(
            model_name='photoalbum',
            name='category_order',
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='category',
            field=models.ForeignKey(to='vingtsunkuen.PhotoAlbum'),
        ),
    ]
