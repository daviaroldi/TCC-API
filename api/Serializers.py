from rest_framework import serializers
from .models import *

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        # fields = '__all__'
        fields = ('id', 'username', 'name', 'gender', 'birthday', 'password')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('id', 'username', 'name', 'gender', 'birthday', 'password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'gender', 'birthday', 'password')
