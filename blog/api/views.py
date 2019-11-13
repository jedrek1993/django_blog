from rest_framework import generics
from ..models import Post
from .serializers import PostSerializer


class PostListViev(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailViev(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
