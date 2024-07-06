import os
from datetime import timedelta, date

import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, \
    Car


# Create queries within functions

def show_all_authors_with_their_books():
    authors_with_their_books = []

    authors = Author.objects.all().order_by("id")

    for author in authors:
        books = author.book_set.all()

        if not books:
            continue

        book_titles = ', '.join(b.title for b in books)
        authors_with_their_books.append(
            f"{author.name} has written - {book_titles}!"
        )

    return '\n'.join(authors_with_their_books)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Song]:
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    rating_sum = sum(r.rating for r in reviews)
    avg_rating = rating_sum / len(reviews)

    return avg_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates() -> str:
    result = []
    all_licenses = DrivingLicense.objects.all().order_by('-license_number')

    for l in all_licenses:
        expiration_date = l.issue_date + timedelta(days=365)
        result.append(f"License with number: {l.license_number} expires on {expiration_date}!")

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet:
    return Driver.objects.filter(license__issue_date__gt=due_date - timedelta(days=365))


def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return (f"Successfully registered {car.model} to {owner.name} "
            f"with registration number {registration.registration_number}.")

