from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from .permissions.IsNotPostRequest import IsNotPostRequest
from .models import *
from _datetime import datetime
import json

from rest_framework import viewsets
from .Serializers import *

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
        # deadline = params['deadline']
        deadline = datetime.strptime(params['deadline'], "%Y-%m-%dT%H:%M:%S.%fZ")
        started_at = datetime.strptime(params['started_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
        deadline = deadline.replace(tzinfo=None)
        started_at = started_at.replace(tzinfo=None)
        professor = Professor.objects.get(id=params['professor'])
        # print(params['deadline'])
        session = Session(
            professor=professor,
            deadline=deadline,
            started_at=started_at,
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
        # sessions = Session.objects.filter(started_at__gte=datetime.now()).order_by('-id')
        print(sessions)

        if ('professor' in params):
            sessions = sessions.filter(professor__pk=params['professor'])

        if ('deadline_lt_now' in params):
            sessions = sessions.filter(deadline__lt=datetime.now())

        if ('student' in params):
            sessions = sessions.filter(students__pk=params['student'])
        serializer = self.get_serializer(sessions, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        params = request.data
        session = Session.objects.get(id=params['session'])
        # options = Option.objects.filter(question_id=)

        question = Question(
            description=params['description'],
            type=params['type'],
            session=session,
            # options=params['options'],
        )
        question.save()
        # print(params)
        if int(params['type']) == 1:
            for opt in params['options']:
                option = Option(
                    label=opt['label'],
                    question_id=question.id,
                )
                option.save()

        serializer = QuestionSerializer(question)

        response = Response(serializer.data)
        # response.set_cookie('Authorization', 'Token ' + token.key)

        return response

    def list(self, request, *args, **kwargs):
        params = request.GET
        questions = Question.objects.all().order_by('-id')
        print(questions)

        if ('session' in params):
            questions = questions.filter(session=params['session'])

        serializer = self.get_serializer(questions, many=True)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        params = request.data
        session = Session.objects.get(id=params['session'])
        # options = Option.objects.get(id=)
        # print(self.get_object())
        # print(params['options'])
        question = self.get_object()
        question.description = params['description']
        question.type = params['type']
        question.session = session

        for opt in params['options']:
            if 'id' in opt:
                options = Option.objects.get(id=opt['id'])
            else:
                options = Option()
            # options = Option.objects.get(id=opt['id'])
            options.label = opt['label']
            options.question_id = question.id

            options.save()

        question.save()
        serializer = QuestionSerializer(question)

        response = Response(serializer.data)

        return response

    def hasAnswer(self, question):
        hasAnswer = False
        #multipla escolha
        if question.type == 1:
            options = Option.objects.filter(question_id=question.id)
            for opt in options:
                answer = Answer.objects.filter(option=opt)
                if answer:
                    hasAnswer = True
        else:
            answers = Answer.objects.filter(question_id=question.id)
            print(answers)
            if answers:
                hasAnswer = True

        return hasAnswer

    def destroy(self, request, *args, **kwargs):
        # print(self.get_object())
        question = self.get_object()

        if not self.hasAnswer(question):
            options = Option.objects.filter(question_id=question.id)
            for opt in options:
                opt.delete()

            question.delete()

            response = Response({'error': False, 'message': 'Excluído com sucesso!'})
        else:
            response = Response({'error': True, 'message': 'Não é possível excluir a pergunta pois há respostas para ela!'})

        return response

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('id')
    serializer_class = AnswerSerializer

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