from django.urls import path, include

from fruitipedia_exam_prep.fruits_app.views import CreateFruitPage, DetailsFruitPage, EditFruitPage, DeleteFruitPage

urlpatterns = [
    path('create', CreateFruitPage.as_view(), name='create-fruit'),
    path('<int:fruitId>/', include([
        path('details/', DetailsFruitPage.as_view(), name='details-fruit'),
        path('edit/', EditFruitPage.as_view(), name='edit-fruit'),
        path('delete/', DeleteFruitPage.as_view(), name='delete-fruit')
    ]))
]
