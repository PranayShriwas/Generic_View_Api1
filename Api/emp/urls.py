from django.urls import path
from .serializers import EmpSerializer
from .api import EmpCreateApi, EmpDeleteApi, EmpGetApi, EmpReteriveApi, EmpUpdateApi
urlpatterns = [
    path('api/create', EmpCreateApi.as_view()),
    path('', EmpGetApi.as_view()),
    path('api/<int:pk>', EmpUpdateApi.as_view()),
    path('api/delete/<int:pk>', EmpDeleteApi.as_view()),
    path('api/reterive/<int:pk>', EmpReteriveApi.as_view())
]
