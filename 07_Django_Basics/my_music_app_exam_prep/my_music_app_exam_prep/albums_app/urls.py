from django.urls import path, include

from my_music_app_exam_prep.albums_app.views import AlbumAddPage, AlbumDetailsPage, AlbumEditPage, AlbumDeletePage

urlpatterns = [
    path('add', AlbumAddPage.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('details/', AlbumDetailsPage.as_view(), name='details-album'),
        path('edit/', AlbumEditPage.as_view(), name='edit-album'),
        path('delete/', AlbumDeletePage.as_view(), name='delete-album')
    ]
    ))
]