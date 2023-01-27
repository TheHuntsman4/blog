from .forms import PostForm

from django.template import loader
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def posts(request):
    posts=Post.objects.all().values()
    return render(request,'blog/post.html',{'posts':posts})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def home(request):
    return render(request,'blog/home.html',{})



