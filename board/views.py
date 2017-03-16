from rest_framework import viewsets, filters

from .models import Employee
from .serializers import EmployeeSerializer

class DefeultsMixin(object):

	filter_backends = (
		filters.DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter,
	)

class EmployeeViewSet(DefeultsMixin, viewsets.ModelViewSet):
	
    queryset = Employee.objects.order_by('id')
    serializer_class = EmployeeSerializer
    search_fields = ('name', 'id')
    ordering_fields = ('id', 'name')