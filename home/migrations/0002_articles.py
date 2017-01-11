# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approwed_article', models.BooleanField(default=True)),
                ('article_img', models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
