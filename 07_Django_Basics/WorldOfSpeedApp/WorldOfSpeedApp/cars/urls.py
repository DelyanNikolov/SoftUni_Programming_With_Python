from django.urls import path, include

from WorldOfSpeedApp.cars.views import catalogue_page, create_car_page, car_details_page, CarEditPage, CarDeletePage

urlpatterns = [
    path('catalogue/', catalogue_page, name='catalogue'),
    path('create/', create_car_page, name='create-car'),
    path('<int:pk>/', include([
        path('details/', car_details_page, name='details-car'),
        path('edit/', CarEditPage.as_view(), name='car-edit'),
        path('delete/', CarDeletePage.as_view(), name='car-delete'),
    ]))
]
