from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import BlogAuthor,BlogPost,BlogComment

# Create your views here.

