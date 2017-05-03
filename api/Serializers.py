from rest_framework import serializers
from .models import *
from pprint import pprint

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        # fields = '__all__'
        # "password": "",
        # "last_login": null,
        # "is_superuser": false,
        # "username": "",
        # "first_name": "",
        # "last_name": "",
        # "email": "",
        # "is_staff": false,
        # "is_active": false,
        # "date_joined": null,
        # "groups": [],
        # "user_permissions": []
        fields = ('id', 'username', 'password', 'is_superuser', 'is_active', 'email', 'first_name', 'last_name')
        read_only_fields = ('is_active','is_superuser',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        professor = Professor(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # password=validated_data['password'],
        )
        professor.is_superuser = True
        professor.set_password(validated_data['password'])
        professor.save()
        return professor

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('id', 'username', 'password', 'is_superuser', 'email', 'first_name', 'last_name')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'name', 'gender', 'birthday', 'password')
