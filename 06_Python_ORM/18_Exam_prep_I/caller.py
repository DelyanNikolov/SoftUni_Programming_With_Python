import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie
from django.db.models import Q, Count, Avg, F


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


def get_actors_by_movies_count() -> str:
    top_three_actors = Actor.objects.annotate(movies_count=Count('movie')).order_by('-movies_count', 'full_name')[:3]

    if not top_three_actors or not top_three_actors[0].movies_count:
        return ""

    result = []
    for actor in top_three_actors:
        result.append(f"{actor.full_name}, participated in {actor.movies_count} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_movie = Movie.objects \
        .select_related('starring_actor') \
        .prefetch_related('actors') \
        .filter(is_awarded=True) \
        .order_by('-rating', 'title') \
        .first()

    if top_movie is None:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'

    participating_actors = top_movie.actors.order_by('full_name').values_list('full_name', flat=True)

    cast = ', '.join(participating_actors)

    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}." \
           f" Starring actor: {starring_actor}. Cast: {cast}."


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies_to_update:
        return 'No ratings increased.'

    updated_movies_count = movies_to_update.count()
    movies_to_update.update(rating=F('rating') + 0.1)
    return f'Rating increased for {updated_movies_count} movies.'

