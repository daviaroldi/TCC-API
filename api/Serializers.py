from rest_framework import serializers
from .models import *
from pprint import pprint

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_professor')
        # read_only_fields = ('is_active','is_superuser',)
        extra_kwargs = {
            'password': {'write_only': True},
            'is_professor': {'read_only': True }
        }

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
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_professor')
        # read_only_fields = ('is_active','is_superuser',)
        extra_kwargs = {
            'password': { 'write_only': True },
            'is_professor': {'read_only': True }
        }

    def create(self, validated_data):
        student = Student(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        student.is_superuser = True
        student.set_password(validated_data['password'])
        student.save()
        return student

class QuestionSerializer(serializers.ModelSerializer):
    # session = SessionSerializer()

    class Meta:
        model = Question
        fields = ('id', 'description')

class SessionSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)
    professor = ProfessorSerializer(read_only=True)
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Session
        fields = ('id', 'code', 'name', 'deadline', 'professor', 'students', 'questions', 'is_open')
        extra_kwargs = {'code': {'read_only': True}, 'is_open': {'read_only': True}}

    # def students(self, obj):
    #     students = Student.objects.filter(session__pk=obj.id)
    #     result = []
    #     for student in students:
    #         result[] = {
    #
    #         }
    #     return {
    #         'professor': {
    #             'name': professor.first_name + ' ' + professor.last_name,
    #             'id': professor.id
    #         }
    #     }

    def create(self, validated_data):
        professor = Professor.objects.filter(id=validated_data['professor'])
        session = Session(
            deadline=validated_data['deadline'],
            name=validated_data['name'],
            professor=professor
        )
        session.save()
        return {
            "id": session.id,
            "code": session.code
        }