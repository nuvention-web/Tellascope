# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150203_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='twitter_oauth_secret',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twitter_oauth_token',
        ),
    ]
