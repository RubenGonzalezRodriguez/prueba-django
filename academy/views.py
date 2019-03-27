from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'academy/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'academy/post_detail.html', {'post': post})

