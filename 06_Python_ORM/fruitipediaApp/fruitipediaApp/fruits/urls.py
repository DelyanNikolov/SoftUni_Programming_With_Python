from django.urls import path

from fruitipediaApp.fruits import views

urlpatterns = (
    path('index/', views.index, name='index'),
)
