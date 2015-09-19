# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150906_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcategory',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
