from django.urls import path

from tasty_recipes_app.common.views import HomePage, CataloguePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('catalogue/', CataloguePage.as_view(), name='catalogue'),
]
