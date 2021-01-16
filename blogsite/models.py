from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import date


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False,default="")
    content = models.TextField(max_length=2000)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)

class BlogComment(models.Model):
    blog= models.ForeignKey(BlogPost, on_delete=models.CASCADE, blank=False,default="")
    comment = models.TextField(max_length=1000, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

        comment_len=75
        if len(self.comment)>comment_len:
            title=self.comment[:comment_len] + '....'
        else:
            title=self.comment
        return title

class BlogAuthor(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=False,default="")
    bio = models.TextField(max_length=400)

    def __str__(self):
        return self.name.username
