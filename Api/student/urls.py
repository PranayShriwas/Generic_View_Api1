from django.urls import path
from .views import StudentReteriveApi, StudentCreateApi, StudentDeleteApi, StudentGetApi, StudentUpdateApi, RegistrationAPIView, LoginAPIView
urlpatterns = [

    path('api/create', StudentCreateApi.as_view()),
    path('', StudentGetApi.as_view()),
    path('api/<int:pk>', StudentUpdateApi.as_view()),
    path('api/delete/<int:pk>', StudentDeleteApi.as_view()),
    path('api/reterive/<int:pk>', StudentReteriveApi.as_view()),
    path('api/registration', RegistrationAPIView.as_view()),
    path('api/login', LoginAPIView.as_view())
]
