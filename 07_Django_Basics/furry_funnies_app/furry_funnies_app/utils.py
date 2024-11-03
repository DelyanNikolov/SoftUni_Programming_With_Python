from furry_funnies_app.author.models import Author


def get_user_obj():
    return Author.objects.first()
