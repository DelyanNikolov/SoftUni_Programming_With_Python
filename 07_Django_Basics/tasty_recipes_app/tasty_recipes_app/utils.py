from tasty_recipes_app.profile_app.models import Profile


def get_user_obj():
    return Profile.objects.first()
