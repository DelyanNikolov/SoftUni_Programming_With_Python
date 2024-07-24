import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Count, Avg
from main_app.models import Book, Author, Publisher


# Create queries within functions
# Let's say we want to get the number of books each author has written:
def get_books_count_by_author() -> str:
    authors_with_books = Author.objects.annotate(book_count=Count('book'))

    result = []
    for author in authors_with_books:
        result.append(f"{author.name} - {author.book_count}")

    return "\n".join(result)


# Suppose we want to get the average rating of all books:
def get_all_books_rating():
    avg_rating = Book.objects.aggregate(avg_rating=Avg('rating'))
    return f"Average book rating is {avg_rating['avg_rating']:.2f}"


# Let's say we want to get the number of books published by each publisher:
def get_number_of_books_by_publisher() -> str:
    publisher_and_books_count = Publisher.objects.annotate(books_count=Count('books')).order_by('-books_count')

    result = []
    for publisher in publisher_and_books_count:
        result.append(f"{publisher.name} - {publisher.books_count}")

    return "\n".join(result)


# Suppose we want to get the average rating of books published by each publisher:
def get_avg_book_rating_by_publisher() -> str:
    publisher_and_rating = Publisher.objects.annotate(avg_rating=Avg('books__rating'))

    result = []
    for publisher in publisher_and_rating:
        result.append(f"{publisher.name} - {publisher.avg_rating:.2f}")

    return "\n".join(result)


# Get the number of books each author has written and the average rating of those books:
def get_number_of_books_by_author_with_avg_rating() -> str:
    authors_with_books = Author.objects.annotate(
        books_count=Count('book'),
        avg_rating=Avg('book__rating')
    ).order_by('-books_count', 'name')

    result = []
    for author in authors_with_books:
        if author.books_count:
            result.append(f"{author.name} - book count: {author.books_count}; avg rating: {author.avg_rating:.2f}")

    return "\n".join(result)


# Get the number of books each publisher has published and the average rating of those books:
def get_number_of_books_by_publisher_with_avg_rating() -> str:
    publisher_and_rating = Publisher.objects.prefetch_related('books').annotate(
        books_count=Count('books'),
        avg_rating=Avg('books__rating')
    )

    result = []
    for publisher in publisher_and_rating:
        if publisher.books_count:
            result.append(f"{publisher.name} - book count{publisher.books_count}"
                          f"avg books rating {publisher.avg_rating:.2f}")

    return '\n'.join(result)


# print(get_books_count_by_author())
# print(get_all_books_rating())
# print(get_number_of_books_by_publisher())
# print(get_avg_book_rating_by_publisher())
# print(get_number_of_books_by_author_with_avg_rating())
print(get_number_of_books_by_publisher_with_avg_rating())
