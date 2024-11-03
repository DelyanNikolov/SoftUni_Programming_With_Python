from django.urls import path

from furry_funnies_app.common.views import IndexPage, DashboardPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard'),
]