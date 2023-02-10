from rest_framework import serializers

from users.models import User, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['username', 'password']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('id', 'api_url', 'user',)
