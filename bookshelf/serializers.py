from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarCode
        fields = ('__all__')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    Code = CodeSerializer()

    class Meta:
        model = Book
        fields = ('url', 'Code', 'title', 'author', 'language', 'Edition')


class LoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = A_Logger
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_user
        fields = ('__all__')
