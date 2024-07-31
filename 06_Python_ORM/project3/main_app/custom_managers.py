from django.db import models
from django.db.models import QuerySet


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self) -> QuerySet:
        authors = self.annotate(
            articles_count=models.Count('articles_authors')
        ).order_by('-articles_count', 'email')

        return authors
