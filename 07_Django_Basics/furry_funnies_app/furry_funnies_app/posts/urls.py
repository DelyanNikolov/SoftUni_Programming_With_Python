from django.urls import path, include

from furry_funnies_app.posts.views import PostCreatePage, PostDetailsPage, PostEditPage, PostDeletePage

urlpatterns = [
    path('create/', PostCreatePage.as_view(), name='create-post'),
    path('<int:post_id>/', include([
        path('details/', PostDetailsPage.as_view(), name='post-details'),
        path('edit/', PostEditPage.as_view(), name='post-edit'),
        path('delete/', PostDeletePage.as_view(), name='post-delete')
    ]))
]
