from django.urls import path

from WorldOfSpeedApp.common.views import home_page

urlpatterns = [
    path('', home_page, name='index'),
]