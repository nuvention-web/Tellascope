# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userarticlerelationship_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userarticlerelationship',
            name='public',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorited_articles',
        ),
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='word_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='followrelationship',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
