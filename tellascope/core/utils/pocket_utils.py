import urlparse
from pocket import Pocket

from datetime import datetime
from tellascope.config.config import SOCIAL_AUTH_POCKET_CONSUMER_KEY

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
	from tellascope.core.models import UserArticleRelationship, Article

	article, created = Article.objects.update_or_create(
		pocket_resolved_id = item['resolved_id'],
		word_count = item['word_count'],
		url = item['resolved_url'],
		title = item['resolved_title'],
		excerpt = item['excerpt'])

	uar, created = UserArticleRelationship.objects.get_or_create(
		pocket_item_id=item['item_id'],
		sharer=user.profile,
		article=article)
	uar.status = item['status']
	uar.pocket_date_added = datetime.utcfromtimestamp(float(item['time_added']))
	uar.pocket_date_updated = datetime.utcfromtimestamp(float(item['time_updated']))

	if item['favorite'] == '1': 
		uar.favorited = True 
	else:
		uar.favorited = False

	print article.title
	uar.save()


def update_user_pocket(user):
	pocket = Pocket(SOCIAL_AUTH_POCKET_CONSUMER_KEY, user.profile.pocket_access_token)
	articles = get_list_from_pocket(pocket)
	for article in articles:
		save_pocket_item_to_database(user, article)
