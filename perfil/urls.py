from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.PerfilView.as_view(), name='perfil')
]
