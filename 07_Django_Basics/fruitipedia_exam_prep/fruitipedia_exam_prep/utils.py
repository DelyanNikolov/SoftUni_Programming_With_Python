from fruitipedia_exam_prep.profile_app.models import Profile


def get_user_obj():
    return Profile.objects.first()