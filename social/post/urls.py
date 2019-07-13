from django.urls import path
from django.contrib import admin
from . import views


app_name = 'post'

urlpatterns = [
	path('', views.PostCreateView.as_view(), name='newsfeed'),
	path('feed/', views.feed, name='feed'),
	path('likes/<int:id>/', views.like_post, name='like_post'),
	path('<int:pk>/comment/', views.add_comment, name='add_comment'),
	path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
