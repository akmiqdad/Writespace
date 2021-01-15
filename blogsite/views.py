from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import BlogPost,BlogComment,BlogAuthor

from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth import authenticate, login
from .forms import CreateBlog,CommentForm,CreateProfile
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def BlogsHome(request):
    blog = BlogPost.objects.all()
    count = BlogPost.objects.all().count()

    p = Paginator(blog, 5)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {}
    context['Blogs'] = blog
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
    bio = BlogAuthor.objects.get(name = Author)
        
    blogs = BlogPost.objects.filter(author = Author)
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

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('author_details')
    else:
        form = UserCreationForm()
    
    context = {}
    context['form'] = form
    return render(request, 'signup.html', context)


def CreateBlog(request):
    if request.method == 'POST':
        form = CreateBlog(request.user.username,request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateBlog(request.username.name)
    
    context = {}
    context['form'] = form
    return render(request,'createblog.html', context)

