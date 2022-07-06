
from django.forms import ModelForm
from posts.models import Post


class FormPost(ModelForm):
    class Meta:
        model = Post
        fields = ('titulo_post', 'conteudo_post', 'excerto_post',
                  'categoria_post', 'imagem_post', 'autor_post')

    def clean(self):
        data = self.cleaned_data
        titulo = data.get('titulo_post')
        conteudo = data.get('conteudo_post')
        excerto = data.get('excerto_post')
        categoria = data.get('categoria_post')
        img = data.get('imagem_post')
        autor = data.get('autor_post')
