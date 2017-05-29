from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from .permissions.IsNotPostRequest import IsNotPostRequest
from .models import *
import json

from rest_framework import viewsets
from .Serializers import ProfessorSerializer, StudentSerializer, SessionSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all().order_by('-username')
    serializer_class = ProfessorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-username')
    serializer_class = StudentSerializer

    permission_classes = ()
    authentication_classes = ()

    def list(self, request, *args, **kwargs):
        recent_users = Student.objects.all().order_by('-id')
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)
#
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('-deadline')
    serializer_class = SessionSerializer

    def create(self, request, *args, **kwargs):
        params = request.data
        deadline = params['deadline']
        professor = Professor.objects.get(id=params['professor'])
        session = Session(
            professor=professor,
            deadline=deadline,
            name=params['name']
        )
        session.save()

        serializer = SessionSerializer(session)

        response = Response(serializer.data)
        # response.set_cookie('Authorization', 'Token ' + token.key)

        return response

    def list(self, request, *args, **kwargs):
        params = request.GET
        sessions = Session.objects.all().order_by('-id')
        if ('professor' in params):
            sessions = sessions.filter(professor__pk=params['professor'])

        if ('student' in params):
            sessions = sessions.filter(students__pk=params['student'])
        serializer = self.get_serializer(sessions, many=True)
        return Response(serializer.data)

# @api_view(['GET'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))aut
# @permission_classes((IsAuthenticated))
# def index(request, format=None):
#     content = {
#         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#         'auth': unicode(request.auth),  # None
#     }
#     return JsonResponse(content)
@api_view(['GET'])
def current_user(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_professor': hasattr(user, 'professor')
    })

@api_view(['GET'])
def login(request):
    token = Token.objects.create(user=request.user)
    response = JsonResponse({'token': token.key})
    # response.set_cookie('Authorization', 'Token ' + token.key)

    return response

# @api_view(['GET'])
# def get_sessions(request):
#     sessions = Session.objects.values('id', 'code', 'name', 'deadline', 'professor', 'students', 'questions')
#     response = JsonResponse(list(sessions), safe=False)
#     # response.set_cookie('Authorization', 'Token ' + token.key)
#
#     return response
    # 'id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_professor'
# @api_view(['POST'])
# @parser_classes((JSONParser,))
# def createSession(request, format=None):
#     params = request.data
#     deadline = params['deadline']
#     professor = Professor.objects.get(id=params['professor'])
#     session = Session(
#         professor=professor,
#         deadline=deadline,
#     )
#     session.save()
#
#     serializer = SessionSerializer(session)
#
#     response = JsonResponse({'session': serializer.data})
#     # response.set_cookie('Authorization', 'Token ' + token.key)
#
#     return response