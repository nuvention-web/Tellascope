# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150301_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_time',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
