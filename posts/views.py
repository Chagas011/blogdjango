
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Post
from .forms import FormPost
from comentarios.forms import FormComentario
from comentarios.models import Comentario

from django.contrib import messages

# Create your views here.


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


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs
        qs = self.model.objects.get_busca(termo)

        return qs


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)
        return qs


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


class PostFormulario(FormView):
    template_name = 'posts/post_formulario.html'
    model = Post
    form_class = FormPost

    def form_valid(self, form):
        post = Post(**form.cleaned_data)
        if self.request.user.is_authenticated:
            post.autor_post = self.request.user
        post.save()
        messages.success(self.request, 'Post enviado com sucesso')
        return redirect('post_index')


"""



class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post
        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user
        comentario.save()
        messages.success(self.request, 'Comentario enviado com sucesso')
        return redirect('post_detalhes', pk=post.id)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(
            publicado_comentario=True, post_comentario=post.id)

        contexto['comentarios'] = comentarios
        return contexto
"""
