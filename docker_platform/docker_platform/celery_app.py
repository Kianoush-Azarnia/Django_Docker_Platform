import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_platform.settings')

# Create the Celery application instance.
app = Celery('docker_platform')

# Load the Celery configuration from Django settings.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover and register tasks from all installed apps.
app.autodiscover_tasks()
