from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import *

from rest_framework import viewsets
from .Serializers import ProfessorSerializer, StudentSerializer

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
        pass
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-username')
#     serializer_class = UserSerializer

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
    response.set_cookie('Authorization', 'Token ' + token.key)

    return response