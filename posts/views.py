
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from .models import Post
from .forms import FormPost
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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


@method_decorator(
    login_required(
        login_url='login_form', redirect_field_name='next'), name='dispatch')
class PostFormulario(FormView):
    template_name = 'posts/post_formulario.html'

    def setup(self, request, *args, **kwargs) -> None:
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': FormPost(request.POST, request.FILES)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = FormPost(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        post = form.save(commit=False)
        if self.request.user.is_authenticated:
            post.autor_post = self.request.user

        post.save()
        messages.success(self.request, 'Post enviado com sucesso')
        return redirect('post_index')


class RegisterView(FormView):
    template_name = 'posts/register_view.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': RegisterForm(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuario criado com sucesso')
        return redirect(reverse('login_form'))


class LoginView(FormView):
    template_name = 'posts/login.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': LoginForm(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Dados invalidos')

        authenticated_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso')
            login(request, authenticated_user)
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Usuario ou senha invalidos')

        return render(request, self.template_name, self.contexto)


@login_required(login_url='login_form', redirect_field_name='next')
def logout_view(request):
    logout(request)
    return redirect('login_form')


@method_decorator(
    login_required(
        login_url='login_form', redirect_field_name='next'), name='dispatch')
class DashboardView(ListView):
    model = Post
    paginate_by = 3
    context_object_name = 'posts'
    template_name = 'posts/dashboard.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(autor_post=self.request.user, publicado_post=False)
        return qs


class DashboardUpdate(UpdateView):
    template_name = 'posts/dashboard_post.html'
    model = Post
    fields = ['titulo_post', 'conteudo_post',
              'excerto_post', 'categoria_post',
              'imagem_post']
    success_url = reverse_lazy('dashboard')


"""
def login_view(request):
    form = LoginForm()
    return render(request, 'posts/login.html', context={
        'form': form,
        'form_action': reverse('login_create'),
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso')
            login(request, authenticated_user)
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Usuario ou senha invalidos')

    else:
        messages.error(request, 'Dados invalidos')

    return redirect('login_form')

"""
