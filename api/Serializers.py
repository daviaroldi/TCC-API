from rest_framework import serializers
from .models import *
from pprint import pprint

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        # read_only_fields = ('is_active','is_superuser',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        professor = Professor(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        professor.is_superuser = True
        professor.set_password(validated_data['password'])
        professor.save()
        return professor

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        # read_only_fields = ('is_active','is_superuser',)
        extra_kwargs = {'password': {'write_only': True}}

class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ('code', 'deadline', 'professor', 'students')

    def create(self, validated_data):
        professor = Professor.objects.filter(id=validated_data['id'])
        session = Session(
            deadline=validated_data['deadline'],
            professor=professor
        )
        session.