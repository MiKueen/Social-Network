from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment
from friends.models import Friend
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

'''
def newsfeed(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data.get('body')
			form.save()
			return render(request, 'users/profile.html')

	else:
		form = PostForm()

	return render(request,'post/newsfeed.html')
'''

class PostCreateView(LoginRequiredMixin, CreateView):
	form_class = PostForm
	template_name = 'post/newsfeed.html'
	success_url = reverse_lazy('users:profile')
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.body = form.cleaned_data.get('body')
		return super(PostCreateView, self).form_valid(form)

def feed(request):
	userids = []
	users = User.objects.exclude(id=request.user.id)
	friend = Friend.objects.get(current_user=request.user)
	friends = friend.users.all()
	for id in friends:
		userids.append(id.id)
		print(id.id)

	#userids.append(friends.id)
	posts = Post.objects.filter(user_id__in=userids)[0:25]
	print(posts)

	return render(request, 'post/newsfeed.html', {'posts': posts})


'''
def like_post(request):
	post = get_object_or_404(Post, id=request.POST.get('id'))
	is_liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
	else:
		post.likes.add(request.user)
		is_liked = True
	return HttpresponseRedirect(post.get_absolute_url())
'''
def like_post(request, id):
    if request.method == 'GET':
        post_id = request.GET.get('id')
        likedpost = Post.objects.get(id=id)
        m = Like(post=likedpost)
        m.user = request.user
        m.save()
        return redirect('/users/profile', id=post_id)
    else:
        return HttpResponse("Request method is not a GET")


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/users/profile', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post/newsfeed.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('/users/profile', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('/users/profile', pk=comment.post.pk)

