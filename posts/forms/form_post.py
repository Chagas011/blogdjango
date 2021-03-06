
from django.forms import ModelForm
from posts.models import Post


class FormPost(ModelForm):
    class Meta:
        model = Post
        fields = ('titulo_post', 'conteudo_post', 'excerto_post',
                  'categoria_post', 'imagem_post', 'autor_post')
