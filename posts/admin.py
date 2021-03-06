from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo_post', 'autor_post', 'data_post',
                    'categoria_post', 'publicado_post',)

    list_editable = ('publicado_post',)
    search_fields = ('id', 'titulo_post', 'autor_post',
                     'categoria_post', 'conteudo_post',)
    list_display_links = ('id', 'titulo_post', 'categoria_post', 'data_post')
    summernote_fields = ('conteudo_post',)
    list_per_page = 5


admin.site.register(Post, PostAdmin)
