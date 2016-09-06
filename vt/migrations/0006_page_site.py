# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vt', '0005_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.CharField(default='vt', max_length=10),
        ),
    ]
