from django.conf.urls import include, url

# from . import views
from rest_framework import routers
# from .views import ProfessorViewSet, StudentViewSet, UserViewSet, index, login
from .views import *
from rest_framework.authtoken import views

# router = routers.DefaultRouter()
# router.register(r'professors', ProfessorViewSet)
# router.register(r'students', StudentViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'', index, name='index'),
    url(r'', login, name='login'),
    # url(r'', include(router.urls))
    url(r'api-token-auth/', views.obtain_auth_token),
]