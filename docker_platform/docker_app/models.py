from django.db import models


class App(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    command = models.CharField(max_length=1000)


class EnvironmentVariable(models.Model):
    app = models.ForeignKey(App, related_name='envs', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Run(models.Model):
    app = models.ForeignKey(App, related_name='runs', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=63, choices=(('Running', 'Running'), ('Finished', 'Finished')))
    parameters = models.CharField(max_length=1000)
