from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    bio = models.CharField(max_length=250, blank=True, null=True)
    profile_picture = models.CharField(max_length=250, blank=True, null=True)

    shared_content = models.ManyToManyField('Content', through='ProfileContentRelationship',
                                           symmetrical=False,
                                           related_name='shared')

    twitter_username = models.CharField(max_length=50, blank=True, null=True)
    twitter_description = models.CharField(max_length=250, blank=True, null=True)
    twitter_profile_picture = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Content(models.Model):
	url = models.URLField(blank=False)
	title = models.CharField(max_length=250, blank=False)
	source = models.CharField(max_length=250, blank=True, null=True)


class ProfileContentRelationship(models.Model):
	sharer = models.ForeignKey(UserProfile, related_name='shared_by')
	content = models.ForeignKey(Content, related_name='shared_content')
	comment = models.CharField(max_length=250, blank=True, null=True)