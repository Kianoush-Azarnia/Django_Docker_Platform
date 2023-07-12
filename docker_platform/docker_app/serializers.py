from rest_framework import serializers
from .models import App, EnvironmentVariable, Run

class EnvironmentVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentVariable
        fields = ['key', 'value']

class AppSerializer(serializers.ModelSerializer):
    envs = EnvironmentVariableSerializer(many=True, read_only=True)

    class Meta:
        model = App
        fields = ['id', 'name', 'image', 'command', 'envs']

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'timestamp', 'status', 'parameters']
