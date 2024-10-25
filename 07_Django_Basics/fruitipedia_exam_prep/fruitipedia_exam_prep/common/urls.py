from django.urls import path

from fruitipedia_exam_prep.common.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
]