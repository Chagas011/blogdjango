from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['titulo_post', 'conteudo_post', 'excerto_post',
                  'categoria_post', 'imagem_post',
                  'autor_post', 'id']
