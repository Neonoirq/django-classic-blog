from django.shortcuts import render

from .models import Post


def home(request):
    return render(request=request, template_name='posts/home.html')


def posts(request):
    post_list = Post.objects.all()
    return render(request=request, template_name='posts/post.html', context={'post_list': post_list})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request=request, template_name='posts/post_detail.html', context={'post': post})