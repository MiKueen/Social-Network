from django.urls import path
from . import views
#from users.views import ProfileView

app_name = 'account'


urlpatterns = [
    path('personal-info/', views.edit_profile, name='personal-info'),
    path('settings/', views.settings, name='settings'),
    path('change-password/', views.change_password, name='change-password'),
    path('hobbies-interest/', views.hobbies_interest, name='hobbies-interest'),
    path('education-employment/', views.education_employment, name='education-employment'),
    path('notifications/', views.notifications, name='notifications'),
    path('chat/', views.chat, name='chat'),
    path('friend-request/', views.FriendView.as_view(), name='friend-request'),
    path('favpage-create/', views.favpage_create, name='favpage-create')
]