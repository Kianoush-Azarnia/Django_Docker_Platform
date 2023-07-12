from django_background_tasks import background
from docker_app.models import App, EnvironmentVariable
import subprocess
import os

@background(schedule=0)  # Decorator to mark the function as a background task
def download_docker_image(app_id, image_address, storage_location):
    # Create the storage location directory if it doesn't exist
    os.makedirs(storage_location, exist_ok=True)

    # Download the Docker image using the `docker pull` command
    subprocess.run(['docker', 'pull', image_address])

@background(schedule=0)
def run_docker_command(app_id):
    # Retrieve the App instance
    app = App.objects.get(id=app_id)

    # Get the command and environment variables associated with the App instance
    command = app.command
    envs = EnvironmentVariable.objects.filter(app_id=app_id)

    # Prepare the environment variables as a list of key-value pairs
    env_list = [f'{env.key}={env.value}' for env in envs]

    # Execute the Docker command using the `docker run` command
    subprocess.run(['docker', 'run', '-e', *env_list, app.image, command])
