from django.shortcuts import render
from django.http import HttpResponse


def posts(request):
    post_list = ['Post1', 'Post2', 'Post3']
    return render(request=request, template_name='posts/post.html', context={'post_list': post_list})



