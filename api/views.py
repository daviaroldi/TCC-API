from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from .models import *

from rest_framework import viewsets
from .Serializers import ProfessorSerializer, StudentSerializer, SessionSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all().order_by('-username')
    serializer_class = ProfessorSerializer

# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-username')
    serializer_class = StudentSerializer

    @authentication_classes([])
    @permission_classes([])
    def list(self, request, *args, **kwargs):
        recent_users = Student.objects.all().order_by('-id')
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)
#
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('-deadline')
    serializer_class = Session

    def create(self, request, *args, **kwargs):
        params = request.data
        deadline = params['deadline']
        professor = Professor.objects.get(id=params['professor'])
        session = Session(
            professor=professor,
            deadline=deadline,
        )
        session.save()

        serializer = SessionSerializer(session)

        response = Response(serializer.data)
        # response.set_cookie('Authorization', 'Token ' + token.key)

        return response

# @api_view(['GET'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated))
# def index(request, format=None):
#     content = {
#         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#         'auth': unicode(request.auth),  # None
#     }
#     return JsonResponse(content)


@api_view(['GET'])
def login(request):
    token = Token.objects.create(user=request.user)
    response = JsonResponse({'token': token.key})
    # response.set_cookie('Authorization', 'Token ' + token.key)

    return response

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