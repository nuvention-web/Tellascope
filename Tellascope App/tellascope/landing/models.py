from django.db import models
# from multiselectfield import MultiSelectField

class EMail(models.Model):
    WORLD = "W"
    US = "U"
    POLITICS = "P"
    BUSINESS = "B"
    TECHNOLOGY = "T"
    SCIENCE = "S"
    SPORTS = "O"
    ARTS = "A"
    FASHION_AND_STYLE = "F"
    INTEREST_CHOICES = (
        (WORLD, 'World News'),
        (US, 'US News'),
        (POLITICS, 'Politics'),
        (BUSINESS, 'Business'),
        (TECHNOLOGY, 'Technology'),
		(SCIENCE, 'Science'),
		(SPORTS, 'Sports'),
		(ARTS, 'Arts'),
		(FASHION_AND_STYLE, 'Fashion and Style')
    )

    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, unique=False, null=True)
    last_name = models.CharField(max_length=100, unique=False, null=True)
    interests = models.CharField(max_length=100, unique=False, null=True)

    # interests = MultiSelectField(choices=INTEREST_CHOICES)

    def __unicode__(self):
    	return self.first_name + ' ' + self.last_name
