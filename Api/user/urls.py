from django.urls import path
from .api import UserCreateApi, UserDeleteApi, UserGetApi, UserReteriveApi, UserUpdateApi
urlpatterns = [
    path('api/create', UserCreateApi.as_view()),
    path('', UserGetApi.as_view()),
    path('api/<int:pk>', UserUpdateApi.as_view()),
    path('api/delete/<int:pk>', UserDeleteApi.as_view()),
    path('api/reterive/<int:pk>', UserReteriveApi.as_view())
]
