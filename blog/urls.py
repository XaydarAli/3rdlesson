from django.urls import path
from .views import PostView,PostDetailView

urlpatterns = [
    path('post/', PostView.as_view(), name='posts-list'),
    path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]