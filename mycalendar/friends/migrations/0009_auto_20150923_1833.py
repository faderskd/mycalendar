# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0008_auto_20150919_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='viewed',
        ),
    ]
