from django.core.management.base import BaseCommand, CommandError
from tellascope.core.models import *
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(args[0], 'rU') as f:
            reader = csv.DictReader(f)
            for row in reader:
            	source = Source.objects.get_or_create(name=row['source'])[0]
            	source.save()
            	author = Author.objects.get_or_create(name=row['author'])[0]
            	author.save()

                article = Article.objects.get_or_create(
                    url=row['url'],
                    title=row['title'],
                    source=source,
                    author=author)[0]

                tags = []
                for tag in row['tags'].split(','):
                    tag = tag.replace('["','').replace('"]','').replace('"','').strip()
                    tags.append(tag)

                for tag in tags:
                    t = Tag.objects.get_or_create(name=tag)[0]
                    t.save()
                    article.tags.add(t)

                article.save()



