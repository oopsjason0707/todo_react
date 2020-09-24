# 회원가입하는 Serializer

from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import User

class SignupSerializer(ModelSerializer):

    password = serializers.CharField(write_only=True)  # read-only 리스트에 보이는데 입력이나 수정에 대해서 권한이 없음
                                                       # wrtie only 패스워드는 안나옴

    class Meta:
        model = User 
        fields = ['username', 'password', 'email', 'phone_number']

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            phone_number = validated_data['phone_number'],
            email = validated_data['email']
            
            
        )
        #얘가 중요. 얘 땜시 위에 만들어줌
        user.set_password(validated_data['password'])
        user.save()
        return user 
