# Docker Model Client Setup Guide

## Project Structure

Create the following files in a directory (e.g., `C:\Users\nyiko\docker-model-client`):

```
docker-model-client/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── app.py
```

## Step-by-Step Instructions

### 1. Create the Project Directory

```bash
cd C:\Users\nyiko
mkdir docker-model-client
cd docker-model-client
```

### 2. Create All Files

Copy the contents from the artifacts into these files:
- `Dockerfile`
- `requirements.txt`
- `app.py`
- `docker-compose.yml` (optional)

### 3. Make Sure Docker Model Runner is Running

Open a **separate terminal** and run:

```bash
docker model run ai/smollm2:latest
```

Leave this running in the background.

### 4. Build the Docker Image

In your project directory, run:

```bash
docker build -t model-client .
```

### 5. Run the Container

**Option A: Using docker run (Windows)**

```bash
docker run --rm --add-host=host.docker.internal:host-gateway model-client
```

**Option B: Using docker run (simpler)**

```bash
docker run --rm --network host model-client
```

**Option C: Using docker-compose**

```bash
docker-compose up
```

## Troubleshooting

### Issue: "Connection refused"

**Solution:** Make sure the Docker Model Runner is running:
```bash
docker model status
```

If not running, start it:
```bash
docker model run ai/smollm2:latest
```

### Issue: "host.docker.internal not found" (Linux)

**Solution:** Replace `host.docker.internal` in `app.py` with your actual host IP:

```python
# Find your host IP first
# On Linux: ip addr show docker0 | grep inet
url = "http://172.17.0.1:12434/v1/chat/completions"
```

### Issue: Port 12434 not accessible

**Solution:** Check if the model runner is listening:
```bash
netstat -an | findstr 12434
```

## Testing Without Docker

Before containerizing, test the script directly:

```bash
python app.py
```

## Customizing the Script

Edit `app.py` to change the queries:

```python
queries = [
    "Your custom question here",
    "Another question",
]
```

## Cleaning Up

Stop and remove containers:
```bash
docker-compose down
```

Remove the image:
```bash
docker rmi model-client
```

## Advanced: Interactive Mode

To run the container interactively:

```bash
docker run -it --rm --network host python:3.11-slim bash
```

Then inside the container:
```bash
pip install requests
python
```

```python
import requests
url = "http://host.docker.internal:12434/v1/chat/completions"
# ... rest of your code
```