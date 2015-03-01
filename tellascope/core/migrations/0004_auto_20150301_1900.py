# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150301_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
