from .serializers import EmpSerializer
from .models import Emp
from rest_framework import generics


class EmpCreateApi(generics.CreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpGetApi(generics.ListAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpUpdateApi(generics.UpdateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpDeleteApi(generics.DestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpReteriveApi(generics.RetrieveAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
