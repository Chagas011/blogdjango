from .post_index import PostIndex


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs
        qs = self.model.objects.get_busca(termo)

        return qs
