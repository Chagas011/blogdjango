from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from perfil.models import Perfils
from django.urls import reverse_lazy
from posts.models import Post
# Isso sera um update view


class PerfilView(TemplateView):
    template_name = 'perfil/perfil.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        perfil_username = context.get('usuario')
        perfil = get_object_or_404(Perfils.objects.filter(
            author__username=perfil_username
        ).select_related('author'), author__username=perfil_username)

        return self.render_to_response({
            **context,
            'perfil': perfil,
            'posts': Post.objects.filter(
                autor_post__username=perfil_username, publicado_post=True)
        })


@method_decorator(
    login_required(
        login_url='login_form', redirect_field_name='next'), name='dispatch')
class PerfilUpdate(UpdateView):
    template_name = 'perfil/perfil_update.html'
    fields = ['bio']
    success_url = reverse_lazy('perfil_update')

    def get(self, request, *args, **kwargs):
        contexto = self.get_context_data(**kwargs)
        perfil = get_object_or_404(Perfils)

        return self.render_to_response({
            **contexto,
            'perfil': perfil,
        })
