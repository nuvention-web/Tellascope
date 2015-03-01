# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150301_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pocket_resolved_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userarticlerelationship',
            name='pocket_item_id',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
