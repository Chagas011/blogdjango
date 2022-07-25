
from rest_framework import serializers
from categorias.models import Categoria


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo_post = serializers.CharField(max_length=255)
    conteudo_post = serializers.CharField(max_length=500)
    categoria_post = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
    )
    categoria_post = serializers.StringRelatedField(source='categoria_post')
