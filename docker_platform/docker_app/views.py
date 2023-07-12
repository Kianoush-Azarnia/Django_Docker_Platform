from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import App, Run
from .serializers import AppSerializer, RunSerializer

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

    def perform_create(self, serializer):
        app_id = self.kwargs['pk']
        app = get_object_or_404(App, id=app_id)
        serializer.save(app=app)


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

