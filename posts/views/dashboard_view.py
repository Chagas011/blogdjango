from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from posts.models import Post


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
