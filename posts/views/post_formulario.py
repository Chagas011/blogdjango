from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from posts.forms import FormPost
from django.shortcuts import redirect, render
from django.contrib import messages


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
