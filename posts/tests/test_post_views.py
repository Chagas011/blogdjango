
from django.test import TestCase
from django.urls import reverse, resolve
from posts import views


class PostViewsTest(TestCase):
    def test_post_home_view(self):
        view = resolve(reverse('post_index'))
        self.assertIs(view.func.view_class, views.PostIndex)

    def test_post_busca_view(self):
        view = resolve(reverse('post_busca'))
        self.assertIs(view.func.view_class, views.PostBusca)

    def test_post_detalhes_view(self):
        view = resolve(reverse('post_detalhes', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.PostDetalhes)

    def test_post_formulario_view(self):
        view = resolve(reverse('post_forms'))
        self.assertIs(view.func.view_class, views.PostFormulario)

    def test_post_register_view(self):
        view = resolve(reverse('register'))
        self.assertIs(view.func.view_class, views.RegisterView)

    def test_post_login_view(self):
        view = resolve(reverse('login_form'))
        self.assertIs(view.func.view_class, views.LoginView)

    def test_post_logout_view(self):
        view = resolve(reverse('logout'))
        self.assertIs(view.func, views.logout_view)

    def test_post_dashboard_view(self):
        view = resolve(reverse('dashboard'))
        self.assertIs(view.func.view_class, views.DashboardView)

    def test_post_dashboard_update_view(self):
        view = resolve(reverse('dashboard_update', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.DashboardUpdate)
