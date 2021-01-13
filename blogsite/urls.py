from django.contrib import admin

from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='home'),
    path('blogger/<author_id>', views.AuthorDetails, name='author_details'),
    path('<blog_id>', views.BlogDetails, name='blog_detail'),
    path('bloggers/', views.Bloggers, name='bloggers'),
    path('<blog_id>/create/', views.CreateComment, name='blog_comment'),
]