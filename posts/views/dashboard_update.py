from django.views.generic.edit import UpdateView
from posts.models import Post
from django.urls import reverse_lazy


class DashboardUpdate(UpdateView):
    template_name = 'posts/dashboard_post.html'
    model = Post
    fields = ['titulo_post', 'conteudo_post',
              'excerto_post', 'categoria_post',
              'imagem_post']
    success_url = reverse_lazy('dashboard')
