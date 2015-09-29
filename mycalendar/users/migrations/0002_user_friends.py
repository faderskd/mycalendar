# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20150919_1319'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(through='friends.Friendship', verbose_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
