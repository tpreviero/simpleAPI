from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.order_by('id')
    serializer_class = EmployeeSerializer
