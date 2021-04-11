from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'civility', 'firstName', 'lastName', 'sexe', 'birthday', 'mail', 'password', 'city', 'country']
