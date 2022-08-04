
from rest_framework.pagination import PageNumberPagination
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet


class PostAPIv1ViewSet(ModelViewSet):
    queryset = posts = Post.objects.get_published()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        qs = super().get_queryset()
        categoria_id = self.request.query_params.get('categoria')

        if categoria_id is not None:
            qs = qs.filter(categoria_post=categoria_id)
        qs = qs.filter()
        return qs
