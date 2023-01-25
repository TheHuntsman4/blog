

from django.template import loader
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    posts=Post.objects.all().values()
    template=loader.get_template("blog/home.html")
    context={
        'posts':posts,
    }

    
    return HttpResponse(template.render(context,request))

