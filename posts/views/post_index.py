from posts.models import Post
from django.views.generic.list import ListView


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('categoria_post')
        qs = self.model.objects.get_published()
        return qs
