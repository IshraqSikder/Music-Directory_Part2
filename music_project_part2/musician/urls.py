from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_musician, name='add_musician'),
    path('register/', views.register, name = 'register'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('logout/', views.user_logout, name = 'logout'),
    path('edit/<int:id>', views.edit_musician, name='edit_musician'),
]