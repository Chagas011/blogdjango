from django.urls import path
from . import views


urlpatterns = [
    path('<str:usuario>', views.PerfilView.as_view(), name='perfila')
]
