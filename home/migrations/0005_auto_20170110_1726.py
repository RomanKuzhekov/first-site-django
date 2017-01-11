# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170109_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='category',
        ),
        migrations.AddField(
            model_name='photos',
            name='Photo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='photos',
            name='Slider_Down',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='photos',
            name='Slider_Up',
            field=models.BooleanField(default=False),
        ),
    ]
