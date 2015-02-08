from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    bio = models.CharField(max_length=250, blank=True, null=True)
    profile_picture = models.CharField(max_length=250, blank=True, null=True)

    shared_articles = models.ManyToManyField('Article', through='UserArticleRelationship',
                                           symmetrical=False,
                                           related_name='shared_by')

    favorited_articles = models.ManyToManyField('Article', related_name='favorited_by')

    following = models.ManyToManyField('self', through='FollowRelationship',
                                           symmetrical=False,
                                           related_name='followed_by')

    topics_followed = models.ManyToManyField('Tag')

    twitter_username = models.CharField(max_length=50, blank=True, null=True)
    twitter_description = models.CharField(max_length=250, blank=True, null=True)
    twitter_profile_picture = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    def share_article(self, article, comment):
    	share, created = UserArticleRelationship.objects.get_or_create(
        	shared_by=self,
        	shared_content=content,
        	comment=comment)
    	return share

    def unshare_article(self, article):
    	UserArticleRelationship.objects.filter(
        	shared_by=self,
        	shared_article=article).delete()
    	return

	def follow_user(self, person):
	    relationship, created = FollowRelationship.objects.get_or_create(
	        from_person=self,
	        to_person=person)
	    return relationship

	def unfollow_user(self, person):
		FollowRelationship.objects.filter(
        	from_person=self,
        	to_person=person).delete()
    	return

    def get_following(self):
    	return self.following.filter(folowees__follower=self)
    
    def get_followers(self):
    	return self.followed_by.filter(followers__followee=self)

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

class Author(models.Model):
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Article(models.Model):
	url = models.URLField(blank=False)
	title = models.CharField(max_length=250, blank=False)
	source = models.ForeignKey('Source', blank=True, null=True, 
									related_name='articles_from_source')
	author = models.ForeignKey('Author', blank=True, null=True, 
									related_name='articles_by_author')
	tags = TaggableManager(through=TaggedArticle)


class UserArticleRelationship(models.Model):
	sharer = models.ForeignKey('UserProfile', related_name='shared_by')
	content = models.ForeignKey('Article', related_name='shared_content')
	comment = models.CharField(max_length=250, blank=True, null=True)
	shared_datetime = models.DateTimeField(auto_now_add=True)

class FollowRelationship(models.Model):
	follower = models.ForeignKey('UserProfile', related_name='followers')
	followee = models.ForeignKey('UserProfile', related_name='followees')
	created_at = models.DateTimeField(auto_now_add=True)

