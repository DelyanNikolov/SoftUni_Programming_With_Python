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
    articles = Article.objects.annotate(
        avg_rating=Avg('articles__rating'),
        num_reviews=Count('articles__rating')
    ).filter(num_reviews__gt=0)

    if not articles.exists():
        return ""

    top_article = articles.order_by('-avg_rating', 'title').first()

    avg_rating = f"{top_article.avg_rating:.2f}"
    num_reviews = top_article.num_reviews
    article_title = top_article.title

    return f"The top-rated article is: {article_title}, with an average rating of {avg_rating}, reviewed {num_reviews} times."


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    try:
        author = Author.objects.prefetch_related('reviews_author').get(email=email)
    except Author.DoesNotExist:
        return "No authors banned."

    num_reviews = author.reviews_author.count()

    author.is_banned = True
    author.save()

    author.reviews_author.all().delete()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."
