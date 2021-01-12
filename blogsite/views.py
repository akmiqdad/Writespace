from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import BlogAuthor,BlogPost,BlogComment

from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth import authenticate, login
# Create your views here.

def blog(request):
    Blogs = BlogPost.objects.all()
    count = BlogPost.objects.all().count()
    p = Paginator(Blogs, 5)

    page_no = request.GET.get('page', 1)

    try:
        page = p.page(page_no)
    except EmptyPage:
        page = p.page(1)
    
    context = {}
    context['Blogs'] = page
    context['Count'] = count
    return render(request,'home.html',context)

def BlogDetails(request,blog_id):
    Blog = BlogPost.objects.get(id=blog_id)
    Comments = BlogComment.objects.filter(blog=BlogPost.objects.get(id=blog_id))
    
    context = {}
    context['Blog'] = Blog
    context['Comments'] = Comments
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        context['User'] = user
    return render(request, 'blogdetails.html', context)

def AuthorDetails(request, author_id):
    Author = User.objects.get(id=author_id)
    try:
        Bio = Bio.objects.get(user = Author)
        default_bio = None
    except Bio.DoesNotExist:
        Bio = None
        default_bio = None
        
    Blogs = BlogPost.objects.filter(blog_author = Author)
    context = {}
    context['Author'] = Author
    context['Bio'] = Bio
    context['Blogs'] = blogs
    return render(request, "profile.html", context)


def CreateComment(request,blog_id):
    if request.method == 'POST':
        form = CommentForm(blog_id,request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = CommentForm(blog_id)

    context = {}
    context['form'] = form
    context['blog_id'] = blog_id
    return render(request,"createcomment.html",context)


def Bloggers(request):
    Bloggers = User.objects.all()
    context = {}
    context['Bloggers'] = Bloggers
    return render(request, "bloggers.html", context)