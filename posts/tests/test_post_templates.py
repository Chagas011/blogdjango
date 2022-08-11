
from posts.models import Post, User
from categorias.models import Categoria

from django.test import TestCase
from django.urls import reverse, resolve
from posts import views


class PostViewTemplatesTest(TestCase):

    def test_post_view_template(self):
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
        )
        ...
