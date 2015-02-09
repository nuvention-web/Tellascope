# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_userprofile_topics_followed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favortied_articles',
            new_name='favorited_articles',
        ),
        migrations.AlterField(
            model_name='taggedarticle',
            name='tag',
            field=models.ForeignKey(related_name=b'taggedarticle_items', to='core.Tag'),
        ),
    ]
