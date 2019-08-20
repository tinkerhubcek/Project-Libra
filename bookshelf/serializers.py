from rest_framework import serializers
from .models import Log_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log_user
        fields=('book','borrower')