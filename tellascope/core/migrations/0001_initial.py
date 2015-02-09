# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True)),
                ('title', models.CharField(max_length=500, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FollowRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('url', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
                ('tag', models.ForeignKey(related_name=b'taggedarticle_items', to='core.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserArticleRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=250, null=True, blank=True)),
                ('shared_datetime', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(related_name=b'shared_article', to='core.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bio', models.CharField(max_length=250, null=True, blank=True)),
                ('profile_picture', models.CharField(max_length=250, null=True, blank=True)),
                ('twitter_username', models.CharField(max_length=50, null=True, blank=True)),
                ('twitter_description', models.CharField(max_length=250, null=True, blank=True)),
                ('twitter_profile_picture', models.CharField(max_length=250, null=True, blank=True)),
                ('favorited_articles', models.ManyToManyField(related_name=b'favorited_by', to='core.Article')),
                ('following', models.ManyToManyField(related_name=b'followed_by', through='core.FollowRelationship', to='core.UserProfile')),
                ('shared_articles', models.ManyToManyField(related_name=b'shared_by', through='core.UserArticleRelationship', to='core.Article')),
                ('topics_followed', models.ManyToManyField(to='core.Tag')),
                ('user', models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userarticlerelationship',
            name='sharer',
            field=models.ForeignKey(related_name=b'shared_by', to='core.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followrelationship',
            name='followee',
            field=models.ForeignKey(related_name=b'followees', to='core.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followrelationship',
            name='follower',
            field=models.ForeignKey(related_name=b'followers', to='core.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(related_name=b'articles_by_author', blank=True, to='core.Author', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.ForeignKey(related_name=b'articles_from_source', blank=True, to='core.Source', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='core.Tag', through='core.TaggedArticle', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
