# Text Summarizer API

This project is a FastAPI-based application that provides text summarization functionality. It is containerized using Docker to make it easy to deploy and run anywhere.

## Prerequisites

Before you start, ensure that you have the following tools installed:

- Docker
- Python 3.11+
- `pip`

## Project Setup

1. **Clone or Download the Project**

   First, download or clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <project-directory>
   Install Dependencies Locally (Optional)
   ```

If you want to install and run the application locally, you can set up the environment using the following steps:

Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the Application Locally (Optional)

To run the FastAPI application locally without Docker:

bash
Copy
Edit
uvicorn main:app --reload
You can then visit http://localhost:8000 to use the application.

Dockerization
To containerize the FastAPI application using Docker, follow the steps below.

1. Create Dockerfile
   A Dockerfile is used to define the environment and instructions for building the Docker image.

The contents of the Dockerfile:

dockerfile
Copy
Edit

# Use official Python image

FROM python:3.11-slim

# Set working directory

WORKDIR /app

# Copy requirements and install

COPY requirements.txt .

# Install dependencies (including uvicorn and fastapi)

RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code

COPY . .

# Expose the port the app will run on

EXPOSE 8000

# Ensure uvicorn is installed

RUN pip install uvicorn

# Start FastAPI app with uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
This Dockerfile:

Uses python:3.11-slim as the base image.

Sets up the working directory as /app.

Installs the required Python packages from requirements.txt.

Ensures that uvicorn (the ASGI server) is installed.

Starts the FastAPI application using uvicorn on port 8000.

2. Build the Docker Image
   In the project directory (where your Dockerfile and requirements.txt are located), run the following command to build the Docker image:

bash
Copy
Edit
docker build -t summarizer-app .
This will build an image tagged summarizer-app.

3. Run the Docker Container
   After the image is successfully built, you can run it as a container:

bash
Copy
Edit
docker run -d -p 8000:8000 summarizer-app
This will run the container in detached mode (-d) and expose port 8000 on your local machine, mapping it to port 8000 inside the container.

4. Verify the Application
   Once the container is running, open your browser or use a tool like curl to verify that the application is running. Navigate to:

FastAPI Docs: http://localhost:8000/docs

Swagger UI: http://localhost:8000/redoc

You should see the interactive documentation for the text summarizer API, where you can input text and receive a summary.

Troubleshooting
Error: uvicorn: executable file not found in $PATH

This error indicates that uvicorn was not installed properly in the container. Ensure that you have included the line RUN pip install uvicorn in your Dockerfile. If you've already built the Docker image, rebuild it after making changes to the Dockerfile.

Rebuild the image with:

bash
Copy
Edit
docker build -t summarizer-app .
Error: permission denied

Ensure that you have the proper permissions to access Docker. Running the command with sudo might help on some systems:

bash
Copy
Edit
sudo docker run -d -p 8000:8000 summarizer-app
API Endpoints
GET /result/{uuid}

Get the summary for a given text identified by its uuid.

Example request:

bash
Copy
Edit
curl -X 'GET' \
 'http://127.0.0.1:8000/result/52f92eed-aa53-462d-9f9e-4e59634b8129' \
 -H 'accept: application/json'
Response:

json
Copy
Edit
{
"status": "Success",
"summary": "FastAPI is a modern, high-performance web framework for building APIs with Python."
}
