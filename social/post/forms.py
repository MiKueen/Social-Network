from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    #content = forms.CharField(max_length=170, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    body = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share your thoughts...'}))

    class Meta:
        model = Post
        fields = ('body',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'body',)

