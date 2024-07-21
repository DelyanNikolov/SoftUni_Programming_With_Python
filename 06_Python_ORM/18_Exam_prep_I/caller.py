import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor
from django.db.models import Q, Count, Avg


# Create queries within functions
def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name is None and search_nationality is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name and search_nationality:
        query = Q(query_name & query_nationality)
    elif search_name:
        query = query_name
    else:
        query = query_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    result = []
    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director() -> str:
    top_director = Director.objects.get_directors_by_movies_count().first()

    if top_director:
        return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."

    else:
        return ""


def get_top_actor():
    top_starring_actor = Actor.objects.prefetch_related('starring_movies').annotate(
        movies_count=Count('starring_movies'),
        avg_rating=Avg('starring_movies__rating')
    ).order_by('-movies_count', 'full_name').first()

    if not top_starring_actor or not top_starring_actor.movies_count:
        return ""

    movies = ', '.join(m.title for m in top_starring_actor.starring_movies.all() if m)

    return (f"Top Actor: {top_starring_actor.full_name},"
            f" starring in movies: {movies}, "
            f"movies average rating: {top_starring_actor.avg_rating:.1f}")

