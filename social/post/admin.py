from django.contrib import admin
from .models import Post, Like, Comment
from .forms import PostForm

class PostModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(Like)
admin.site.register(Comment)
