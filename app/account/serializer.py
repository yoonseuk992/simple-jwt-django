from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        new_password = validated_data.pop('new_password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(new_password)
        instance.save()
        return instance

    class Meta:
        fields = ('new_password', 'email', 'first_name', 'last_name')
        model = User
