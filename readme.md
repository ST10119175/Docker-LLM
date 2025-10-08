# Dockerized Local LLM with Streamlit UI

## Overview

This project demonstrates a self-contained, portable AI application that runs a local Large Language Model (LLM) and exposes it through a user-friendly web interface built with Streamlit. The entire application stack is containerized using Docker and orchestrated with Docker Compose, making it easy to set up and run on any machine with Docker installed.

The application consists of two main services:
1.  **Model Service**: Downloads and serves a specified open-source LLM, providing an OpenAI-compatible API endpoint.
2.  **Streamlit UI Service**: A web-based chat interface that communicates with the model service, allowing users to interact with the LLM.

---

## For Recruiters: Skills Demonstrated

This project showcases proficiency in several key areas of modern software and MLOps engineering:

*   **Containerization & Orchestration**:
    *   **Docker**: Creating reproducible and isolated environments for both the frontend and the AI model backend.
    *   **Docker Compose**: Defining and managing a multi-service application, including networking, volumes for data persistence, and health checks.

*   **Microservices Architecture**:
    *   Designing a decoupled system where the user interface (`streamlit-app`) and the AI model inference (`model-runner`) are independent services that communicate over a network.

*   **AI/ML Integration**:
    *   Experience with running and serving Large Language Models locally.
    *   Configuration of model parameters (e.g., `MODEL_NAME`, `MAX_TOKENS`) via environment variables.

*   **Backend & Frontend Development**:
    *   **Python**: The core language for the entire stack.
    *   **Streamlit**: Rapidly developing an interactive and user-friendly web UI for an AI application.

*   **Configuration Management**:
    *   Using `.env` files to manage environment-specific configurations and secrets securely, separating configuration from code.

---

## Architecture

The `docker-compose.yml` file orchestrates the following services:

*   `streamlit-app`: The frontend service built from a local `Dockerfile`. It serves a Streamlit application on port `8501` and communicates with the model service.
*   `model-runner` (Implied): A backend service that runs the LLM and exposes an API on port `12434`. The Streamlit app is configured to connect to this service.

Services communicate over a custom Docker bridge network, ensuring they can resolve each other by their service names.

---

## How to Run

### Prerequisites

*   Docker
*   Docker Compose

### 1. Configuration

The project is configured using the `.env` file. You can adjust the model name, port, and other parameters here. The default configuration is set to run a small, efficient model.

```shell
# .env
BASE_URL=http://host.docker.internal:12434/engines/v1
MODEL_NAME=ai/smollm2:latest
MAX_TOKENS=500
TEMPERATURE=0.7
```

### 2. Launch the Application

Open a terminal in the project's root directory and run the following command:

```bash
docker-compose up --build -d
```

*   On the first run, Docker will download the base images and the LLM, which may take a few minutes depending on your network speed.
*   The `-d` flag runs the containers in detached mode.

### 3. Access the Application

Once the containers are running, open your web browser and navigate to:

**`http://localhost:8501`**

You should see the Streamlit chat interface, ready to interact with the local LLM.

### 4. Shut Down

To stop and remove the containers, run:

```bash
docker-compose down
```