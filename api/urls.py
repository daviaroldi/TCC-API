from django.conf.urls import include, url

# from . import views
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views



router = routers.DefaultRouter()
router.register(r'professors', ProfessorViewSet)
router.register(r'students', StudentViewSet)
router.register(r'session', SessionViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    # url(r'', index, name='index'),
    url(r'user-info', current_user, name='current_user'),
    url(r'session-connect', connect_session, name='connect_session'),
    # url(r'get-sessions', get_sessions, name='get_sessions'),
    url(r'', include(router.urls)),
    url(r'login', views.obtain_auth_token),
    # url(r'create-session/', createSession, name='createSession'),
]