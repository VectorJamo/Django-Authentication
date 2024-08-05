from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register_user, name='register-user'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='user_auth/login.html'), name='login-user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_auth/logout.html'), name='logout-user'),
]