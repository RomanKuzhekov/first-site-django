# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_img', models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='images/')),
                ('category', models.ForeignKey(to='home.Category')),
            ],
        ),
    ]
