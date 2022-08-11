from .test_post_templates import PostViewTemplatesTest
from rest_framework import test
from posts.models import Post, User
from categorias.models import Categoria


class ApiPostTest(test.APITestCase, PostViewTemplatesTest):
    def test_post_api_list(self):
        api_url = '/posts/api/v1/'
        response = self.client.get(api_url)
        self.assertEqual(
            response.status_code, 200
        )

    def make_post(self):
        categoria = Categoria.objects.create(nome_cat='TESTE')
        author = User.objects.create_user(
            first_name='usertes',
            last_name='userteste',
            username='user',
            password='user123',
            email='user@user.com',
        )

        post = Post.objects.create(
            titulo_post='Post Test',
            autor_post=author,
            conteudo_post='POST DE TESTE',
            excerto_post='TESTANDO AQUI Ó',
            categoria_post=categoria,
            publicado_post=True
        )
        return post

    def test_post_api_list_load(self):
        post = self.make_post()
        api_url = '/posts/api/v1/'
        response = self.client.get(api_url)

        print(response.data)
