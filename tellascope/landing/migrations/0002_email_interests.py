# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='interests',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
