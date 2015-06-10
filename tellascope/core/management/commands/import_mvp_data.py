from django.core.management.base import BaseCommand, CommandError
from tellascope.core.models import *
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(args[0], 'rU') as f:
            reader = csv.DictReader(f)

            user, created = User.objects.get_or_create(username='ekoh')
            user.set_password('password')
            user.save()
            profile, created = UserProfile.objects.get_or_create(user=user)

            for x in range(0, 50):
                u, created = User.objects.get_or_create(username='user' + str(x))
                u.set_password('password')
                u.save()
                p, created = UserProfile.objects.get_or_create(user=u)
                if x < 30:
                    profile.follow_user(p)

            for row in reader:
            	source, created = Source.objects.get_or_create(name=row['source'])
            	author, created = Author.objects.get_or_create(name=row['author'])
                article, created = Article.objects.get_or_create(
                    url=row['url'],
                    title=row['title'],
                    source=source,
                    author=author)

                for tag in row['tags'].split(','):
                    tag = tag.replace('["','').replace('"]','').replace('"','').strip()
                    t, created = Tag.objects.get_or_create(name=tag)
                    article.tags.add(tag)

                for x in range(0, int(row['num_shares'])):
                    u = User.objects.filter(username='user' + str(x))[0]
                    p = UserProfile.objects.filter(user=u)[0]
                    p.share_article(article)

                print '\n'
