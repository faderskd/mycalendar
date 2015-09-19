# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventcategory',
            name='user',
            field=models.ForeignKey(default=1, related_name='event_categories', verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('user', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='eventcategory',
            unique_together=set([('name', 'user')]),
        ),
    ]
