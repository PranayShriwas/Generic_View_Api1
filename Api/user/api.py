from .serializers import UserSeializer
from .models import user
from rest_framework import generics


class UserCreateApi(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSeializer


class UserGetApi(generics.ListAPIView):
    queryset = user.objects.all()
    serializer_class = UserSeializer


class UserUpdateApi(generics.UpdateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSeializer


class UserDeleteApi(generics.DestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSeializer


class UserReteriveApi(generics.RetrieveAPIView):
    queryset = user.objects.all()
    serializer_class = UserSeializer
