from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from friends.models import Friend
from django.urls import reverse_lazy
from .multiforms import MultiFormsView
from datetime import datetime
from .forms import EditProfileForm, ProfileForm
from django.contrib.auth.decorators import login_required

User = get_user_model()


def settings(request):
    return render(request,'account/account-settings.html')

def change_password(request):
    return render(request,'account/account-change-password.html')

def hobbies_interest(request):
    return render(request,'account/account-hobbies-interest.html')

def education_employment(request):
    return render(request,'account/account-education-employment.html')

def notifications(request):
    return render(request,'account/account-notifications.html')

def chat(request):
    return render(request,'account/account-chat-messages.html')

def favpage_create(request):
    return render(request,'account/account-favpage-create.html')


class FriendView(TemplateView):
    template_name = 'account/account-friend-request.html'

    def get(self, request):
        
        try:
            users = User.objects.exclude(id=request.user.id)
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friend = None
            friends = None

        args = {'users': users, 'friends': friends}
        return render(request, self.template_name, args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user_form = user_form
            custom_form.save()
            return redirect('/users/profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    args = {'form': form, 'profile_form': profile_form}
        
    return render(request, 'account/account-personal-info.html', args)
