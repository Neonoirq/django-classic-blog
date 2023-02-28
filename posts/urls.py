from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.home, name='home_page_url'),
    path('posts/', views.posts, name='posts_list_url'),
    path('posts/<str:slug>/', views.post_detail, name='post_detail_url'),
]