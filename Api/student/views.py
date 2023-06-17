from django.shortcuts import render
from .serializers import StudentSerializer, LoginSerializer
from .models import Student
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
# Create your views here.


class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGetApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateApi(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentReteriveApi(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request):
        data = request.POST.copy()
        password = data.get('password')
        data['password'] = make_password(password)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        refresh = RefreshToken.for_user(student)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(token)


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        Stu_email = serializers.validated_data['Stu_email']
        password = serializers.validated_data['password']

        try:
            student = Student.objects.get(Stu_email=Stu_email)
        except Student.DoesNotExist:
            return Response({'error': 'Invalid Email.'}, status=400)
        if not check_password(password, student.password):
            return Response({'error': 'Invalid Password.'}, status=400)
        refresh = RefreshToken.for_user(student)
        response_data = {
            'email': Stu_email,
            'access_token': str(refresh.access_token),
        }
        return Response(response_data)
