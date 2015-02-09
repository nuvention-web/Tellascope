# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150203_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
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
                ('followee', models.ForeignKey(related_name=b'followees', to='core.UserProfile')),
                ('follower', models.ForeignKey(related_name=b'followers', to='core.UserProfile')),
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
            name='UserArticleRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=250, null=True, blank=True)),
                ('shared_datetime', models.DateTimeField(auto_now_add=True)),
                ('content', models.ForeignKey(related_name=b'shared_content', to='core.Article')),
                ('sharer', models.ForeignKey(related_name=b'shared_by', to='core.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
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
            model_name='userprofile',
            name='favortied_articles',
            field=models.ManyToManyField(related_name=b'favorited_by', to='core.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(related_name=b'followed_by', through='core.FollowRelationship', to='core.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='shared_articles',
            field=models.ManyToManyField(related_name=b'shared_by', through='core.UserArticleRelationship', to='core.Article'),
            preserve_default=True,
        ),
    ]
