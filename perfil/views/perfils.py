from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from perfil.models import Perfils


@method_decorator(
    login_required(
        login_url='login_form', redirect_field_name='next'), name='dispatch')
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
            'perfil': perfil
        })
