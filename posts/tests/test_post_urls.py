from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class PostURLSTest(TestCase):

    def test_post_home_url(self):
        url = reverse('post_index')
        self.assertEqual(url, '/')

    def test_post_categoria_url(self):
        url = reverse('post_categoria', args=('python',))
        self.assertEqual(url, '/categoria/python')

    def test_post_busca_url(self):
        url = reverse('post_busca')
        self.assertEqual(url, '/busca/')

    def test_post_detalhes_url(self):
        url = reverse('post_detalhes', kwargs={'pk': 1})
        self.assertEqual(url, '/posts/1')

    def test_post_formulario_url(self):
        url = reverse('post_forms')
        self.assertEqual(url, '/posts/formulario')

    def test_post_register_url(self):
        url = reverse('register')
        self.assertEqual(url, '/register')

    def test_post_login_url(self):
        url = reverse('login_form')
        self.assertEqual(url, '/login')

    def test_post_logout_url(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout')

    def test_post_dashboard_url(self):
        url = reverse('dashboard')
        self.assertEqual(url, '/dashboard')

    def test_post_dashboard_update_url(self):
        url = reverse('dashboard_update', kwargs={'pk': 1})
        self.assertEqual(url, '/dashboard/post/1')
