
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from perfil.models import Perfils


class PerfilView(TemplateView):
    template_name = 'perfil/perfil.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        perfil_id = context.get('id')
        perfil = get_object_or_404(
            Perfils.objects.filter
            (pk=perfil_id).select_related('author'), pk=perfil_id)
        return self.render_to_response({
            **context,
            'perfil': perfil
        })
