# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0009_auto_20150923_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('receiver', models.ForeignKey(related_name='received_friendships_requests', to=settings.AUTH_USER_MODEL, verbose_name='receiver')),
                ('sender', models.ForeignKey(related_name='sent_friendship_requests', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
            ],
            options={
                'verbose_name': 'FriendshipRequest',
                'verbose_name_plural': 'FriendshipRequests',
                'ordering': ('created',),
            },
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='sender',
        ),
        migrations.DeleteModel(
            name='FriendshipRequest',
        ),
    ]
