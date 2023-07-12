from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import App, Run
from .serializers import AppSerializer, RunSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RunViewSet(viewsets.ModelViewSet):
    serializer_class = RunSerializer

    def get_queryset(self):
        app_id = self.kwargs['pk']
        return Run.objects.filter(app_id=app_id)

    def perform_create(self, serializer):
        app_id = self.kwargs['pk']
        app = get_object_or_404(App, id=app_id)
        serializer.save(app=app)

