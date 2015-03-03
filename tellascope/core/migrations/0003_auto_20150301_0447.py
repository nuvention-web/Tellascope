# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150301_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
