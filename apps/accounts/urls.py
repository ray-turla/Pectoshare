from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),
    name='login'),
  path('logout', auth_views.LogoutView.as_view(), name='logout'),
  path('register/', views.Register.as_view(), name='register'),
  path('profile/<slug>', views.Profile.as_view(), name='profile'),
  path('profile/edit/<slug>/<int:pk>', views.EditProfile.as_view(), name='edit_profile'),
]