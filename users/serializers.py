from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
  
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        exclude = ['groups','user_permissions','last_login']
        
    def create(self,validated_data):
        validated_data['is_active'] = True
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        print('User Created')
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups','user_permissions','last_login','password']
