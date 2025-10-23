from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import PatientSerializer


class PatientListCreateView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]


class PatientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_fields = ['name', 'last_name']
