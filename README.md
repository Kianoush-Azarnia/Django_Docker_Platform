# D-Docker Platform

D-Docker is a Django web application that allows users to manage and run Docker containers. It provides a user-friendly interface for creating and managing Docker-based applications.

## Technologies Used

The project utilizes the following technologies:

- **Django**: Django is a powerful Python web framework used for building web applications. It provides the core functionality and structure of the Docker Platform.

- **Django REST Framework**: Django REST Framework is a toolkit for building RESTful APIs with Django. It is used to create the API endpoints for managing Docker containers and applications.

- **Celery**: Celery is a distributed task queue system implemented in Python. It is used for asynchronous task processing, allowing background tasks to be executed independently from the main application.

- **RabbitMQ**: RabbitMQ is a message broker that enables communication between the Django application and Celery workers. It handles the task queue and distributes tasks to the appropriate worker processes.

- **Docker**: Docker is a containerization platform that allows applications to be packaged into containers. Docker Platform leverages Docker to create and manage the Docker containers used by the applications.

## Functionality

Docker Platform provides the following functionality:

- **App Creation**: Users can create new Docker applications by specifying the application name, Docker image, and command to run.

- **App Management**: Users can view, update, and delete existing Docker applications. They can also view the status and logs of running containers.

- **Docker Image Download**: When creating an application, the system automatically downloads the specified Docker image from a remote repository using the `docker pull` command.

- **Docker Container Execution**: Docker Platform launches Docker containers for each application and executes the specified command inside the container.

- **Asynchronous Task Processing**: The application utilizes Celery and RabbitMQ to execute time-consuming tasks asynchronously. This ensures a smooth user experience and improves performance.

## Getting Started

To run the Docker Platform locally, follow these steps:

1. Clone the repository from GitHub: `git clone https://github.com/your-username/docker-platform.git`

2. Install the required dependencies: `pip install -r requirements.txt`

3. Set up the database and apply migrations: `python manage.py migrate`

4. Start the Django development server: `python manage.py runserver`

5. Access the application in your web browser at `http://localhost:8000`

That's it! You can now use Docker Platform to manage and run your Docker containers with ease.

Feel free to explore the project's source code and make any necessary modifications to fit your requirements.

Enjoy using Docker Platform!

> Note: The above instructions assume you have Docker and other necessary dependencies installed on your local machine.
