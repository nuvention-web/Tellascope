# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='facebook_share_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='twitter_share_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
