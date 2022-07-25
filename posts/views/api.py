
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Post
from ..serializers import PostSerializer
from rest_framework import status


@api_view()
def post_api_list(request):
    posts = Post.objects.get_published()
    serializer = PostSerializer(instance=posts, many=True)
    return Response(serializer.data)


@api_view()
def post_api_detail(request, pk):
    post = Post.objects.get_published().filter(pk=pk).first()

    if post:
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)

    else:

        return Response({
            'detail': 'Nada encontrado'
        }, status=status.HTTP_404_NOT_FOUND)
