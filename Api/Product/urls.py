# from django.urls import path
# from .serializers import EmpSerializer
# from .api import EmpCreateApi, EmpDeleteApi, EmpGetApi, EmpReteriveApi, EmpUpdateApi
# urlpatterns = [
#     path('api/create', EmpCreateApi.as_view()),
#     path('', EmpGetApi.as_view()),
#     path('api/<int:pk>', EmpUpdateApi.as_view()),
#     path('api/delete/<int:pk>', EmpDeleteApi.as_view()),
#     path('api/reterive/<int:pk>', EmpReteriveApi.as_view())
# ]

from django.urls import path
from .views import ProductCreateApi, ProductDeleteApi, ProductGetApi, ProductReteriveApi, ProductUpdateApi
from .models import Product
urlpatterns = [
    path('api/create', ProductCreateApi.as_view()),
    path('', ProductGetApi.as_view()),
    path('api/<int:pk>', ProductUpdateApi.as_view()),
    path('api/delete/<int:pk>', ProductDeleteApi.as_view()),
    path('api/reterive/<int:pk>', ProductReteriveApi.as_view())
]
