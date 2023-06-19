from django.urls import path
from .views import LaptopApi, LaptopCreateApi, LaptopDeleteApi, LaptopUpdateApi, LaptopReteriveApi
urlpatterns = [

    path('api/create', LaptopCreateApi.as_view()),
    path('', LaptopApi.as_view()),
    path('api/<int:pk>', LaptopUpdateApi.as_view()),
    path('api/delete/<int:pk>', LaptopDeleteApi.as_view()),
    path('api/reterive/<int:pk>', LaptopReteriveApi.as_view()),
]
