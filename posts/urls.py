from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter


post_api_v1_router = SimpleRouter()
post_api_v1_router.register('posts/api/v1', views.PostAPIv1ViewSet)


urlpatterns = [
    path('', views.PostIndex.as_view(), name='post_index'),

    path('categoria/<str:categoria>',
         views.PostCategoria.as_view(),
         name='post_categoria'),

    path('busca/',
         views.PostBusca.as_view(),
         name='post_busca'),

    path('posts/<int:pk>',
         views.PostDetalhes.as_view(),
         name='post_detalhes'),

    path('posts/formulario',
         views.PostFormulario.as_view(),
         name='post_forms'),

    path('register',
         views.RegisterView.as_view(),
         name='register'),

    path('login',
         views.LoginView.as_view(),
         name='login_form'),

    path('logout',
         views.logout_view,
         name='logout'),

    path('dashboard',
         views.DashboardView.as_view(),
         name='dashboard'),

    path('dashboard/post/<int:pk>',
         views.DashboardUpdate.as_view(),
         name='dashboard_update'),

]

urlpatterns += post_api_v1_router.urls
