from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo_post = serializers.CharField(max_length=255)
    conteudo_post = serializers.CharField(max_length=500)
    categoria_post = serializers.StringRelatedField()
    autor_post = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    author_links = serializers.HyperlinkedRelatedField(
        source='autor_post',
        queryset=User.objects.all(),
        view_name='post_api_v1_user',
    )
