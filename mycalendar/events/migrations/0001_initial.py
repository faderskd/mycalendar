# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='desription')),
                ('start', models.DateTimeField(verbose_name='start time')),
                ('end', models.DateTimeField(verbose_name='end time')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('color', colorful.fields.RGBColorField(verbose_name='color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(to='events.EventCategory', verbose_name='category', related_name='events'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='events'),
        ),
    ]
