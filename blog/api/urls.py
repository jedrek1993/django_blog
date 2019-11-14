from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('comments', views.CommentViewSet)


app_name = 'blog_api'

urlpatterns = [
    path('posts/',
        views.PostListViev.as_view(),
        name='post_list'),
    path('posts/<pk>/',
        views.PostDetailViev.as_view(),
        name='post_detail'),
    path('posts/<pk>/add_comment/',
        views.CommentAddView.as_view(),
        name='add_comment'),
    path('', include(router.urls)),
]
