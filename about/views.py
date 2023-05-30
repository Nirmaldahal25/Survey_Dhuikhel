from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from about.models import About
from about.serializers import AboutFormSerializer
# Create your views here.

class AboutListCreateView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = About.objects.all()
    serializer_class = AboutFormSerializer

    def get_queryset(self):
        queryset = super(AboutListCreateView, self).get_queryset()
        name = self.request.query_params.get("name")
        citizenship = self.request.query_params.get("mobile_number")
        if name and citizenship:
            queryset = queryset.filter(name=name, citizenship=citizenship)
        return queryset
    
class AboutRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = AboutFormSerializer
    queryset = About.objects.all()
