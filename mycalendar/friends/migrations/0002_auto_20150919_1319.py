# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='accepted',
        ),
        migrations.AddField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(blank=True, choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], max_length=8, verbose_name='status'),
        ),
    ]
