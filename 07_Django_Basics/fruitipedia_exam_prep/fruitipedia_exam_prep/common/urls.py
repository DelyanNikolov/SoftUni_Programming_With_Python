from django.urls import path

from fruitipedia_exam_prep.common.views import IndexPage, DashboardPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard'),
]
