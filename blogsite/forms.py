from django import forms
from .models import BlogPost,BlogComment,BlogAuthor

from django.contrib.auth.models import User


class CreateProfile(forms.ModelForm):

    class Meta:
        model = BlogAuthor
        fields = ('name', 'bio')

    def __init__(self, user, *args, **kwargs):
        super(CreateProfile, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(username=user)

class CreateBlog(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title' ,'author' ,'content')

    def __init__(self, user, *args, **kwargs):
        super(CreateBlog, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(username=user)

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('blog' , 'comment')

    def __init__(self, blog_id, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = BlogPost.objects.filter(id = blog_id)
