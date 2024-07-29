import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
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

    if not directors.exists():
        return ""

    result = []
    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()

    if top_director is None:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."


def get_top_actor():
    top_starring_actor = Actor.objects.prefetch_related('starring_actors').annotate(
        movies_count=Count('starring_actors'), avg_rating=Avg('starring_actors__rating')
    ).order_by('-movies_count', 'full_name').first()

    movies = Movie.objects.filter(starring_actor=top_starring_actor).all()

    if top_starring_actor is None or not movies.exists():
        return ""

    return (f"Top Actor: {top_starring_actor.full_name}, "
            f"starring in movies: {', '.join(m.title for m in movies)}, "
            f"movies average rating: {top_starring_actor.avg_rating:.1f}")


def get_actors_by_movies_count():
    actors = Actor.objects.prefetch_related('actors').annotate(
        movies_count=Count('actors')).order_by('-movies_count', 'full_name').filter(movies_count__gt=0)[:3]

    if not actors.exists():
        return ""

    result = []
    for a in actors:
        result.append(f"{a.full_name}, participated in {a.movies_count} movies")
    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_rated_movie = (Movie.objects.select_related('starring_actor').prefetch_related('actors').filter(is_awarded=True).
                       order_by('-rating', 'title')).first()

    if top_rated_movie is None:
        return ""

    starring_actor = top_rated_movie.starring_actor.full_name if top_rated_movie.starring_actor is not None else 'N/A'
    cast = (a.full_name for a in top_rated_movie.actors.order_by('full_name'))

    return (f"Top rated awarded movie: {top_rated_movie.title}, "
            f"rating: {top_rated_movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {', '.join(cast)}.")


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)
    if not movies_to_update:
        return "No ratings increased."
    updated_movies_count = movies_to_update.count()
    movies_to_update.update(rating=F('rating') + 0.1)
    return f"Rating increased for {updated_movies_count} movies."


print(get_top_rated_awarded_movie())