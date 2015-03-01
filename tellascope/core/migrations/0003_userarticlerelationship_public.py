# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150223_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='userarticlerelationship',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
