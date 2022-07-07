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
    path('register', views.register_view, name='register'),
    path('register/create', views.register_create, name='register_create'),
    path('login', views.login_view, name='login_form'),
    path('login/create', views.login_create, name='login_create'),
    path('logout', views.logout_view, name='logout'),
]
