from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post 
# Create your views here.

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    return render(request, 'blog/detail.html', {'post':post})


def list_posts(request):
    posts = get_list_or_404(Post)
    return render(request, 'blog/list.html', {'posts':posts})