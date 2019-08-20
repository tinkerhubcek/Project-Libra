from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=A_Logger
        fields=('__all__')
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('__all__')