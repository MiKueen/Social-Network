from django.urls import path
from django.contrib import admin
from . import views


app_name = 'friends'

urlpatterns = [
	path('', views.FriendView.as_view(), name='followers'),
	path('connect/<str:operation>/<int:pk>/', views.change_friends, name='change_friends'),
]
