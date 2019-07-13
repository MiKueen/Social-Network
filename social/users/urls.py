from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
	UserRegisterView, ProfileView
	)
#from post.views import like_post

app_name = 'users'

urlpatterns = [
	path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    #path('likes/', like_post, name='like_post'),
]