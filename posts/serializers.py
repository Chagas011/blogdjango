
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo_post = serializers.CharField(max_length=255)
    conteudo_post = serializers.CharField(max_length=500)
