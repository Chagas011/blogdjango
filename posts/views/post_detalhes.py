from django.views import View
from django.shortcuts import redirect, get_object_or_404, render
from comentarios.models import Comentario
from comentarios.forms import FormComentario
from django.contrib import messages

from posts.models import Post


class PostDetalhes(View):
    template_name = 'posts/post_detalhes.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publicado_post=True)
        self.contexto = {
            'post': post,
            'comentarios': Comentario.objects.
            filter(post_comentario=post, publicado_comentario=True),
            'form': FormComentario(request.POST or None),
        }

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']
        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        comentario = form.save(commit=False)
        if request.user.is_authenticated:
            comentario.usuario_comentario = request.user

        comentario.post_comentario = self.contexto['post']
        comentario.save()
        messages.success(self.request, 'Comentario enviado com sucesso')
        return redirect('post_detalhes', pk=self.kwargs.get('pk'))
