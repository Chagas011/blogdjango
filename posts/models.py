from django.db.models import Q, Count, Case, When
from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class PostsManager(models.Manager):
    def get_published(self):
        return self.filter(
            publicado_post=True
        ).annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        ).order_by('-id')

    def get_busca(self, termo):
        return self.filter(
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |
            Q(excerto_post__iexact=termo) |
            Q(conteudo_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )


class Post(models.Model):
    objects = PostsManager()
    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    autor_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteudo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=True, null=True,
        verbose_name='Categoria')
    imagem_post = models.ImageField(
        upload_to='post_img/%Y/%m/%d',
        blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self) -> str:
        return self.titulo_post
