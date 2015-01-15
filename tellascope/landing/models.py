from django.db import models
from django.forms import ModelForm

class EMail(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, unique=False, null=True)
    last_name = models.CharField(max_length=100, unique=False, null=True)

    def __unicode__(self):
    	return self.name
