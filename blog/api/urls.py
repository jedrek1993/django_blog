from django.urls import path
from . import views


app_name = 'blog_api'

urlpatterns = [
    path('posts/',
        views.PostListViev.as_view(),
        name='post_list'),
    path('posts/<pk>/',
        views.PostDetailViev.as_view(),
        name='post_detail'),
]
