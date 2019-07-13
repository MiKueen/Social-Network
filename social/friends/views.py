from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from post.models import Post

from .models import Friend

class FriendView(TemplateView):
	template_name = 'friends/followers.html'

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

def change_friends(request, operation, pk):
	friend = User.objects.get(pk=pk)
	if operation == 'add':
		Friend.make_friend(request.user, friend)
	elif operation == 'remove':
		Friend.lose_friend(request.user, friend)
	return redirect('friends:followers')

