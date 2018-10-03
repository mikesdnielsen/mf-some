from django.urls import path

from .views import PostCreateView, PostDetailView, PostListView

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
]
