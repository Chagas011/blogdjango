from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='post_index'),
    path('categoria/<str:categoria>',
         views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('posts/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
    path('posts/formulario',
         views.PostFormulario.as_view(), name='post_forms'),
]
