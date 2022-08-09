from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('', views.PostIndex.as_view(), name='post_index'),

    path(
        'categoria/<str:categoria>',
        views.PostCategoria.as_view(),
        name='post_categoria'),

    path(
        'busca/',
        views.PostBusca.as_view(),
        name='post_busca'),

    path(
        'posts/<int:pk>',
        views.PostDetalhes.as_view(),
        name='post_detalhes'),

    path(
        'posts/formulario',
        views.PostFormulario.as_view(),
        name='post_forms'),

    path(
        'register',
        views.RegisterView.as_view(),
        name='register'),

    path(
        'login',
        views.LoginView.as_view(),
        name='login_form'),

    path(
        'logout',
        views.logout_view,
        name='logout'),

    path(
        'dashboard',
        views.DashboardView.as_view(),
        name='dashboard'),

    path(
        'dashboard/post/<int:pk>',
        views.DashboardUpdate.as_view(),
        name='dashboard_update'),

    path(
        'posts/api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'posts/api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    path(
        'posts/api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),

]
post_api_v1_router = SimpleRouter()
post_api_v1_router.register('posts/api/v1', views.PostAPIv1ViewSet)

urlpatterns += post_api_v1_router.urls
