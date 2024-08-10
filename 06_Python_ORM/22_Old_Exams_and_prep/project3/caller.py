import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review


# Create queries within functions
def get_authors(search_name=None, search_email=None) -> str:
    if search_name is None and search_email is None:
        return ""
    search_by_name = Q(full_name__icontains=search_name)
    search_by_email = Q(email__icontains=search_email)

    if search_name is not None and search_email is not None:
        query = Q(search_by_name & search_by_email)
    elif search_name is not None:
        query = search_by_name
    else:
        query = search_by_email

    authors = Author.objects.filter(query).order_by('-full_name', )

    if not authors.exists():
        return ""

    result = []
    for a in authors:
        status = "Banned" if a.is_banned else "Not Banned"
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {status}")

    return "\n".join(result)


def get_top_publisher() -> str:
    top_published_author = Author.objects.get_authors_by_article_count().first()

    if top_published_author is None or top_published_author.articles_count == 0:
        return ""

    return (f"Top Author: {top_published_author.full_name} "
            f"with {top_published_author.articles_count} published articles.")


def get_top_reviewer():
    top_reviewed_author = Author.objects.annotate(
        reviews_count=Count('reviews_author')
    ).order_by('-reviews_count', 'email').first()

    if top_reviewed_author is None or top_reviewed_author.reviews_count == 0:
        return ""

    return (f"Top Reviewer: {top_reviewed_author.full_name} with "
            f"{top_reviewed_author.reviews_count} published reviews.")


def get_latest_article() -> str:
    last_article = Article.objects.prefetch_related(
        'reviews', 'authors'
    ).order_by(
        '-published_on'
    ).annotate(
        num_reviews=Count('reviews'),
        avg_reviews_rating=Avg('reviews__rating')
    ).first()

    if last_article is None:
        return ""

    authors_names = ', '.join(a.full_name for a in last_article.authors.order_by('full_name'))
    average_rating = last_article.avg_reviews_rating if last_article.avg_reviews_rating is not None else 0.00
    return (f"The latest article is: {last_article.title}. "
            f"Authors: {authors_names}. "
            f"Reviewed: {last_article.num_reviews} times. "
            f"Average Rating: {average_rating:.2f}.")


def get_top_rated_article() -> str:
    top_article = Article.objects.prefetch_related(
        'reviews',
    ).annotate(
        num_reviews=Count('reviews'),
        avg_rating=Avg('reviews__rating')
    ).order_by(
        '-avg_rating', 'title'
    ).first()

    if top_article is None or top_article.num_reviews == 0:
        return ""

    average_rating = top_article.avg_rating if top_article.avg_rating is not None else 0.00

    return (f"The top-rated article is: {top_article.title}, "
            f"with an average rating of {average_rating:.2f}, "
            f"reviewed {top_article.num_reviews} times.")


def ban_author(email=None):
    if email is None:
        return "No authors banned."
    author_to_ban = Author.objects.prefetch_related(
        "reviews_author"
    ).annotate(
        reviews_count=Count("reviews_author")
    ).filter(
        email__iexact=email
    ).first()

    if author_to_ban is None:
        return "No authors banned."

    num_reviews = author_to_ban.reviews_count

    author_to_ban.is_banned = True
    author_to_ban.save()

    author_to_ban.reviews_author.all().delete()

    return f"Author: {author_to_ban.full_name} is banned! {num_reviews} reviews deleted."


print(ban_author('Author 4'))