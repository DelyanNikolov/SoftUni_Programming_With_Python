import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review
from django.db.models import Q, Count


# Create queries within functions
def get_authors(search_name=None, search_email=None) -> str:
    if search_name is None and search_email is None:
        return ""

    elif search_name is not None and search_email is None:
        query = Q(full_name__icontains=search_name)
    elif search_email is not None and search_name is None:
        query = Q(email__icontains=search_email)
    else:
        query = Q(full_name__icontains=search_name, email__icontains=search_email)

    authors = Author.objects.filter(query).order_by('-full_name')
    if not authors.exists():
        return ""

    result = []
    for a in authors:
        status = "Banned" if a.is_banned is True else "Not Banned"
        result.append(f"Author: {a.full_name}, email: {a.email},"
                      f" status: {status}")
    return '\n'.join(result)


def get_top_publisher() -> str:
    top_publisher = Author.objects.annotate(
        articles_count=Count("article")
    ).order_by(
        "-articles_count", 'email'
    ).filter(articles_count__gt=0).first()

    if top_publisher is None:
        return ""
    return (f"Top Author:"
            f" {top_publisher.full_name} with {top_publisher.articles_count} published articles.")


def get_top_reviewer() -> str:
    top_reviewer = (
        Author.objects.annotate(
            reviews_count=Count("review")
        ).filter(
            reviews_count__gt=0
        ).order_by("-reviews_count").first())

    if top_reviewer is None:
        return ""

    return (f"Top Reviewer: {top_reviewer.full_name} "
            f"with {top_reviewer.reviews_count} published reviews.")
