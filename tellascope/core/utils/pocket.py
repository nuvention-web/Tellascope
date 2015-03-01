import urlparse
from pocket import Pocket

from datetime import datetime
from tellascope.config.config import SOCIAL_AUTH_POCKET_CONSUMER_KEY

from tellascope.core import models

def clean_url(url):
	parse = urlparse.urlparse(url)
	url = parse.scheme + "://" + parse.netloc + parse.path
	return url

def get_list_from_pocket(pocket):
    articles, header = pocket.get(state='all')
    article_list = []
    for key, value in articles.get('list').iteritems():
        article_list.append(value)
    return article_list

def save_pocket_item_to_database(user, item):
	uar = models.UserArticleRelationship.objects.get_or_create(pocket_item_id=item['item_id'])
	uar.status = item['status']
	uar.pocket_date_added = datetime.utcfromtimestamp(item['time_added'])
	uar.pocket_date_updated = datetime.utcfromtimestamp(item['time_updated'])
	uar.sharer = user.profile

	if item['favorited'] == '1': 
		uar.favorited = True 
	else:
		uar.favorited = False

	article = models.Article.objects.get_or_create(pocket_resolved_id=item.resolved_id)
	article.word_count = item.word_count
	article.url = item.resolved_url
	article.title = item.resolved_title
	article.excerpt = item.excerpt

	article.save()
	uar.article = article
	uar.save()

def update_user_pocket(user):
	pocket = Pocket(SOCIAL_AUTH_POCKET_CONSUMER_KEY, user.profile.pocket_access_token)
	articles = get_list_from_pocket(pocket)
	for article in articles:
		save_pocket_item_to_database(user, article)



