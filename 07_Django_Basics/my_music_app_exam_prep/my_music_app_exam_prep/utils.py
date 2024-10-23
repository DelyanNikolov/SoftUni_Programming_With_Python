from my_music_app_exam_prep.profiles_app.models import Profile


def get_user_obj():
    return Profile.objects.first()
