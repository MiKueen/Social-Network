from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UserRegisterForm
from .models import UserProfile
from friends.models import Friend
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

User = get_user_model()

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        #first_name = form.cleaned_data.get("first_name")
        #last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)

class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friend = None
            friends = None

        args = {'users': users, 'friends': friends}
        return render(request, self.template_name, args)
