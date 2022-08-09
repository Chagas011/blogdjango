
from rest_framework.pagination import PageNumberPagination
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from ..permissoes_api import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response


class PostAPIv1ViewSet(ModelViewSet):
    queryset = Post.objects.get_published()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        categoria_id = self.request.query_params.get('categoria')

        if categoria_id is not None:
            qs = qs.filter(categoria_post=categoria_id)
        qs = qs.filter()
        return qs

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Post.objects.get_published(), pk=pk)

        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE', ]:
            return [IsOwner()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(autor_post=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
