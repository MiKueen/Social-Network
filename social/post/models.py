from django.db import models
from django.contrib.auth.models import User
from .validators import validate_content
from django.utils import timezone

class Post(models.Model):
  user = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
  body = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  likes = models.ManyToManyField(User, related_name='likes', blank=True)

  class Meta:
    ordering = ('-created_at',)

  def __str__(self):
  	return self.body

  def total_likes(self):
    return self.likes.count()

class Like(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post',on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    #user = models.ForeignKey(User, related_name='post_user', on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.body

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
