# Docker Exploration

Project live at: https://docker-hello.azurewebsites.net/
This is a simple Python application that displays "Hello, World!" along with the number of times you have visited the page. The goal of building this project was to learn and practice using Docker.

## Github Actions Workflow

GitHub Actions workflow defined in the .github/workflows directory. This workflow is configured to run whenever there is a push or pull request on the main branch.

The "create-docker-image" job in the GitHub Actions workflow initiates on each commit to the main branch, running on an Ubuntu environment, checking out code, building the latest Docker image, and pushing it to Docker Hub using provided credentials.

## CI/CD to Azure at : https://docker-hello.azurewebsites.net/

- Docker images are automatically deployed to Azure.
- Webhooks are set up to trigger a Docker pull in Azure when the CI workflow completes.
## Docker Image

The Docker image for this application is hosted on Docker Hub with the name `aryanspillai/helloworld`. You can find it [here](https://hub.docker.com/r/aryanspillai/helloworld).

## How to Run Locally

To run the application using Docker Compose, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/aryan619348/docker-exploration.git

2. Change into the project directory:

    ```bash
    cd docker-exploration

3. Run the application using Docker Compose:

    ```bash
    docker-compose up -d

This command will start the application in detached mode, and you can access it in your web browser at http://localhost:8000.


To stop the application, use the following command:

    docker-compose down
