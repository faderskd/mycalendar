# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0007_auto_20150919_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='from_user',
            field=models.ForeignKey(verbose_name='from user', related_name='sent_friendships', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friendship',
            name='to_user',
            field=models.ForeignKey(verbose_name='to user', related_name='received_friendships', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('from_user', 'to_user')]),
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='sender',
        ),
    ]
