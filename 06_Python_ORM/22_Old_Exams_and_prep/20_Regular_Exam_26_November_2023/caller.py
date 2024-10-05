import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review
from django.db.models import Q, Count, Avg


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


def get_latest_article() -> str:
    latest_article = Article.objects.order_by('-published_on').first()

    if latest_article is None:
        return ""

    authors = latest_article.authors.order_by('full_name')
    author_names = ", ".join(author.full_name for author in authors)

    reviews = Review.objects.filter(article=latest_article)
    num_reviews = reviews.count()
    avg_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']

    avg_rating = f"{avg_rating:.2f}" if avg_rating is not None else "0.00"

    result = (
        f"The latest article is: {latest_article.title}. "
        f"Authors: {author_names}. "
        f"Reviewed: {num_reviews} times. "
        f"Average Rating: {avg_rating}."
    )
    return result


def get_top_rated_article():
    top_article = Article.objects.annotate(
        avg_rating=Avg('review__rating'), reviews_count=Count('review')
    ).filter(reviews_count__gt=0).order_by('-avg_rating', 'title').first()

    if top_article is None or top_article.reviews_count == 0:
        return ""

    return (f"The top-rated article is:"
            f" {top_article.title}, with an average rating of {top_article.avg_rating:.2f}, "
            f"reviewed {top_article.reviews_count} times.")


def ban_author(email=None):
    author = Author.objects.prefetch_related('review_set').filter(email__exact=email).first()
    if email is None or author is None:
        return "No authors banned."

    reviews_count = author.review_set.count()
    author.is_banned = True
    author.save()
    author.review_set.all().delete()

    return f"Author: {author.full_name} is banned! {reviews_count} reviews deleted."
