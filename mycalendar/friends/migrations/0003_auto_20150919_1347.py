# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20150919_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friendshiprequest',
            options={'verbose_name_plural': 'FriendshipRequests', 'verbose_name': 'FriendshipRequest', 'ordering': ('created',)},
        ),
    ]
