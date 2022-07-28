
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Post
from ..serializers import PostSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status


@api_view(http_method_names=['get', 'post'])
def post_api_list(request):
    if request.method == 'GET':

        posts = Post.objects.get_published().select_related(
            'categoria_post', 'autor_post')
        serializer = PostSerializer(
            instance=posts,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['get', 'patch', 'delete'])
def post_api_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(
            instance=post,
            many=False,
            context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PostSerializer(
            instance=post,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def post_api_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    serializer = UserSerializer(
        instance=user,
        context={'request': request}
    )
    return Response(serializer.data)
