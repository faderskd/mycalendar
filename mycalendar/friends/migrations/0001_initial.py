# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('receiver', models.ForeignKey(related_name='received_friendships', verbose_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sent_friendships', verbose_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friendship',
                'verbose_name_plural': 'Friendships',
            },
        ),
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('viewed', models.BooleanField(verbose_name='viewed', default=False)),
                ('accepted', models.NullBooleanField(verbose_name='accepted', default=None)),
                ('receiver', models.ForeignKey(related_name='received_friendships_requests', verbose_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sent_friendship_requests', verbose_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FriendshipRequest',
                'verbose_name_plural': 'FriendshipRequests',
            },
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('sender', 'receiver')]),
        ),
    ]
