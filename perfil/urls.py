from django.urls import path

from . import views


urlpatterns = [
    path('<str:usuario>', views.PerfilView.as_view(), name='perfila'),
    path('update/<int:pk>', views.PerfilUpdate.as_view(), name='perfil_update')
]
