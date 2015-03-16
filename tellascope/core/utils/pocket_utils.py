import urlparse
from pocket import Pocket

from datetime import datetime
from django.utils import timezone

from tellascope.config.config import SOCIAL_AUTH_POCKET_CONSUMER_KEY

def clean_url(url):
	parse = urlparse.urlparse(url)
	url = parse.scheme + "://" + parse.netloc + parse.path
	return url

def get_list_from_pocket(pocket):
    articles, header = pocket.get(state='all', detailType='complete', contentType='article')
    article_list = []
    for key, value in articles.get('list').iteritems():
        article_list.append(value)
    return article_list

def save_pocket_item_to_database(user, item):
	from tellascope.core.models import Article, UserArticleRelationship, Author

	if 'mailto' in item['resolved_url']:
		return

	article, created = Article.objects.get_or_create(
		pocket_resolved_id = item['resolved_id'], defaults = {
			'word_count': item['word_count'],
			'url': clean_url(item['resolved_url']),
			'title': item['resolved_title'],
			'excerpt': item['excerpt']})

	if 'authors' in item.keys():
		for key, value in item['authors'].iteritems():

			if 'mailto' in value['url']:
				return

			author, created = Author.objects.get_or_create(
				pocket_author_id = value['author_id'], defaults={
					'url': clean_url(value['url']),
					'name': value['name']
				})
	    	article.authors.add(author)

	uar, created = UserArticleRelationship.objects.get_or_create(
		pocket_item_id=item['item_id'],
		sharer=user.profile,
		article=article)
	uar.pocket_status = item['status']
	uar.pocket_date_added = timezone.make_aware(
								datetime.utcfromtimestamp(float(item['time_added'])),
								timezone.get_current_timezone())
	uar.pocket_date_updated = timezone.make_aware(
								datetime.utcfromtimestamp(float(item['time_updated'])),
								timezone.get_current_timezone())

	if item['favorite'] == '1': 
		uar.favorited = True 
	else:
		uar.favorited = False

	article.word_count = int(item['word_count'])
	article.read_time = int(float(item['word_count'])/180)
	article.save(force_update=True)
	print article.read_time

	print article.title
	uar.save()


def update_user_pocket(user):
	pocket = Pocket(SOCIAL_AUTH_POCKET_CONSUMER_KEY, user.profile.pocket_access_token)
	articles = get_list_from_pocket(pocket)
	print len(articles)
	for article in articles:
		try:
			save_pocket_item_to_database(user, article)
		except:
			pass
