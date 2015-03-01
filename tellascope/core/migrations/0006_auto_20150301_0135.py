# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150301_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userarticlerelationship',
            old_name='pocket_id',
            new_name='pocket_item_id',
        ),
        migrations.AddField(
            model_name='article',
            name='pocket_resolved_id',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userarticlerelationship',
            name='pocket_date_read',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userarticlerelationship',
            name='pocket_date_updated',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userarticlerelationship',
            name='pocket_status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Unread'), (b'1', b'Archived')]),
        ),
    ]
