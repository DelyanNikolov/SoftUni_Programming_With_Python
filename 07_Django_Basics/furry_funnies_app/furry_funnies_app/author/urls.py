from django.urls import path

from furry_funnies_app.author.views import AuthorCreatePage, AuthorDetailsPage, AuthorEditPage, AuthorDeletePage

urlpatterns = [
    path('create/', AuthorCreatePage.as_view(), name='author-create_page'),
    path('details/', AuthorDetailsPage.as_view(), name='author-details'),
    path('edit/', AuthorEditPage.as_view(), name='author-edit'),
    path('delete/', AuthorDeletePage.as_view(), name='author-delete'),
]
