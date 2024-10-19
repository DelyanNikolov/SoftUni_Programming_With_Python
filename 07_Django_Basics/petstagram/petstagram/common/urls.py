from django.urls import path

from petstagram.common import views
from petstagram.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>', views.copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>', views.comment_functionality, name='comment'),
]
