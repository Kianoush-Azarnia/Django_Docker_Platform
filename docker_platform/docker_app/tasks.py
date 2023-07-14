from celery import shared_task
from docker_app.models import App, EnvironmentVariable
import subprocess
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

@shared_task
def download_docker_image(app_id, image_address, storage_location):
    # Create the storage location directory if it doesn't exist
    os.makedirs(storage_location, exist_ok=True)

    # Download the Docker image using the `docker pull` command
    subprocess.run(['docker', 'pull', image_address])

    # Save the Docker image to the desired location
    image_name = image_address.split('/')[-1]  # Extract the image name from the address
    image_path = os.path.join(storage_location, image_name)

    subprocess.run(['docker', 'save', '-o', image_path, image_address])

    # Optionally, you can extract the image to a directory
    # if you want to access its contents directly
    extraction_dir = os.path.join(storage_location, 'extracted')
    os.makedirs(extraction_dir, exist_ok=True)

    subprocess.run(['tar', 'xf', image_path, '-C', extraction_dir])

    # If you want to use Django's FileSystemStorage to manage the saved image,
    # you can save it using the storage system
    fs = FileSystemStorage(location=storage_location)
    saved_image_path = fs.save(image_name, open(image_path, 'rb'))

    # Clean up the temporary image file
    os.remove(image_path)

    return saved_image_path

@shared_task
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
