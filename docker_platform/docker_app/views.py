from django.shortcuts import render

from rest_framework import viewsets
from .models import App, Run
from .serializers import AppSerializer, RunSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

