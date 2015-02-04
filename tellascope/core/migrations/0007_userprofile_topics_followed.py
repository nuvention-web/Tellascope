# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150204_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='topics_followed',
            field=models.ManyToManyField(to='core.Tag'),
            preserve_default=True,
        ),
    ]
