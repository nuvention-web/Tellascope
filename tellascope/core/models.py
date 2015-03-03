from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase

from tellascope.core import utils
from tellascope.config.config import SOCIAL_AUTH_POCKET_CONSUMER_KEY

import pocket
import django_filters

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    bio = models.CharField(max_length=250, blank=True, null=True)
    profile_picture = models.CharField(max_length=250, blank=True, null=True)

    shared_articles = models.ManyToManyField('Article', 
                                    through='UserArticleRelationship',
                                    symmetrical=False,
                                    related_name='shared_by')

    following = models.ManyToManyField('self', through='FollowRelationship', 
                                        symmetrical=False,
                                        related_name='followed_by')

    topics_followed = models.ManyToManyField('Tag')

    twitter_username = models.CharField(max_length=50, blank=True, null=True)
    twitter_description = models.CharField(max_length=250, blank=True, null=True)
    twitter_profile_picture = models.CharField(max_length=250, blank=True, null=True)

    # Auth Information
    twitter_oauth_token = models.CharField(max_length=250, blank=True, null=True)
    twitter_oauth_token_secret = models.CharField(max_length=250, blank=True, null=True)
    pocket_access_token = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    def __save__(self):
        super(UserProfile, self).save(*args, **kwargs)
        self.pocket = pocket.Pocket(SOCIAL_AUTH_POCKET_CONSUMER_KEY, self.pocket_access_token)

    def share_article(self, article, comment=''):
        share, created = UserArticleRelationship.objects.get_or_create(
            sharer=self,
            article=article,
            comment=comment)
        return share

    def unshare_article(self, article):
        UserArticleRelationship.objects.filter(
            sharer=self,
            article=article).delete()
        return

    def follow_user(self, profile):
        relationship, created = FollowRelationship.objects.get_or_create(
            follower=self,
            followee=profile)
        return relationship

    def unfollow_user(self, profile):
        FollowRelationship.objects.filter(
            follower=self,
            folowee=profile).delete()
        return

    def get_following(self):
        return self.following.filter(followees__follower=self)
    
    def get_followers(self):
        return self.followed_by.filter(followers__follower=self)

    def get_mutual_followers(self):
        return self.following.filter(
            folowees__follower=self,
            followers__followee=self)

class Tag(TagBase):
    pass

class TaggedArticle(GenericTaggedItemBase):
    tag = models.ForeignKey('Tag', related_name="%(class)s_items")

class Source(models.Model):
    name = models.CharField(max_length=250, blank=True)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250, blank=True)
    url = models.URLField(max_length=500, blank=False, null=True)
    pocket_author_id = models.CharField(max_length=100, null=True, unique=True)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    url = models.URLField(max_length=1000, blank=False, null=True)
    title = models.CharField(max_length=500, blank=False, null=True)
    excerpt = models.TextField(blank=True, null=True)
    source = models.ForeignKey('Source', blank=True, null=True, 
                                    related_name='articles_from_source')
    authors = models.ManyToManyField('Author')
    tags = TaggableManager(through=TaggedArticle, blank=True)
    word_count = models.IntegerField(blank=False, null=True)
    pocket_resolved_id = models.CharField(max_length=100, null=True, unique=True)

    def __unicode__(self):
        return self.title

    @property
    def clean_url(self):
        return utils.clean_url(self.url);

    @property
    def read_time(self):
        minutes = self.word_count / 200
        return timedelta(minutes=minutes)


class UserArticleRelationship(models.Model):

    UNREAD = '0'
    ARCHIVE = '1'
    STATUS_OPTIONS = (
        (UNREAD, 'Unread'),
        (ARCHIVE, 'Archived'),
    )

    sharer = models.ForeignKey('UserProfile', related_name='shared_by')
    article = models.ForeignKey('Article', related_name='shared_article')
    comment = models.CharField(max_length=250, blank=True, null=True)
    shared_datetime = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    #From Pocket API
    pocket_item_id = models.CharField(max_length=100, unique=True)
    pocket_status = models.CharField(max_length=1,
                                      choices=STATUS_OPTIONS,
                                      default=UNREAD)
    pocket_favorited = models.BooleanField(default=False)
    pocket_date_added = models.DateTimeField(blank=True, null=True)
    pocket_date_updated = models.DateTimeField(blank=True, null=True)
    pocket_date_read = models.DateTimeField(blank=True, null=True)


class FollowRelationship(models.Model):
    follower = models.ForeignKey('UserProfile', related_name='followers')
    followee = models.ForeignKey('UserProfile', related_name='followees')
    created_at = models.DateTimeField(blank=True)

