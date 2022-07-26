
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Post
from ..serializers import PostSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


@api_view()
def post_api_list(request):
    posts = Post.objects.get_published().select_related(
        'categoria_post', 'autor_post')
    serializer = PostSerializer(
        instance=posts,
        many=True,
        context={'request': request},
    )
    return Response(serializer.data)


@api_view()
def post_api_detail(request, pk):
    post = get_object_or_404(Post, pk=pk).select_related(
        'categoria_post', 'autor_post')
    serializer = PostSerializer(instance=post, context={'request': request})
    return Response(serializer.data)


@api_view()
def post_api_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    serializer = UserSerializer(
        instance=user,
        context={'request': request}
    )
    return Response(serializer.data)
