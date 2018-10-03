from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserListView.as_view(), name='list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('invite/user/<int:pk>/', views.UserInviteView.as_view(), name='invite'),
    path('invite/accept/<int:pk>/', views.UserAcceptInviteView.as_view(), name='accept'),
]
