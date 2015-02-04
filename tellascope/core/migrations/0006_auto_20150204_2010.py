# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('core', '0005_auto_20150204_0352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaggedArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(related_name='core_taggedarticle_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(related_name=b'core_taggedarticle_items', to='core.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='core.Tag', through='core.TaggedArticle', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
