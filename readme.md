# 🤖 Docker-Based LLM Chat Application

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)

A production-ready, containerized chatbot application leveraging Docker Model Runner for local LLM inference. This project demonstrates modern DevOps practices, containerization, and AI integration without relying on external API services.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technical Stack](#technical-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Highlights](#technical-highlights)
- [Future Enhancements](#future-enhancements)

## 🎯 Overview

This project showcases the development of a fully containerized AI chatbot that runs entirely on local infrastructure using Docker Model Runner. It eliminates external API dependencies while maintaining a professional, production-ready architecture suitable for enterprise deployment.

**Key Achievement:** Successfully integrated Docker's experimental Model Runner feature with a modern web application, demonstrating adaptability to emerging technologies and ability to work with cutting-edge tools.

## ✨ Key Features

- **🐳 Fully Containerized**: Complete Docker-based deployment with isolated services
- **🔒 Privacy-First**: All AI processing happens locally - no data leaves your infrastructure
- **💬 Real-Time Chat**: Interactive conversational interface with message history
- **📊 Health Monitoring**: Built-in service health checks and status monitoring
- **🎨 Modern UI**: Clean, responsive Streamlit interface with dark mode support
- **🔧 Configurable**: Environment-based configuration for easy deployment across environments
- **📈 Production-Ready**: Includes health checks, auto-restart policies, and proper error handling

## 📸 Screenshot

<img width="1907" height="866" alt="image" src="https://github.com/user-attachments/assets/5a486cc3-f5af-47db-b95a-f6327f31845b" />


## 🛠 Technical Stack

### Core Technologies
- **Backend Framework**: Python 3.11
- **Web Framework**: Streamlit 1.31.0
- **AI Integration**: OpenAI SDK (compatible with local models)
- **Containerization**: Docker & Docker Compose
- **Model Runtime**: Docker Model Runner (Ollama-based)

### Key Libraries
```
streamlit==1.31.0
openai==1.12.0
python-dotenv==1.0.0
requests==2.31.0
```

### Infrastructure
- Docker Desktop with Model Runner enabled
- Multi-container orchestration with Docker Compose
- Bridge networking for service isolation
- Volume persistence for model caching

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Client Browser                        │
│                   (localhost:8501)                       │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTP
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Streamlit Container                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  - Chat Interface                                │   │
│  │  - Session Management                            │   │
│  │  - Health Monitoring                             │   │
│  └─────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────┘
                        │ OpenAI-Compatible API
                        │ (host.docker.internal:12434)
                        ▼
┌─────────────────────────────────────────────────────────┐
│           Docker Model Runner Service                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │  - LLM Inference Engine                          │   │
│  │  - Model: SmolLM2-135M (Quantized)              │   │
│  │  - API Endpoint: /engines/v1                     │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Design Decisions

1. **Microservices Architecture**: Separated concerns with dedicated containers for UI and inference
2. **OpenAI SDK Compatibility**: Leveraged industry-standard SDK for easy model swapping
3. **Environment-Based Config**: Follows 12-factor app principles for configuration management
4. **Health Checks**: Implemented container health monitoring for reliability
5. **Volume Persistence**: Cached models to reduce startup time and bandwidth usage

## 🚀 Installation

### Prerequisites

- Docker Desktop (with Model Runner enabled)
- 4GB+ RAM available
- Windows 10/11, macOS, or Linux

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Docker-LLM
   ```

2. **Enable Docker Model Runner**
   - Open Docker Desktop
   - Navigate to Settings → Features in development
   - Enable "Docker Model Runner"
   - Enable "Enable host-side TCP support"
   - Set port to `12434`
   - Apply & Restart

3. **Pull the AI model**
   ```bash
   docker model pull ai/smollm2:135M-Q4_K_M
   ```

4. **Configure environment**
   ```bash
   # .env file is already configured
   # Verify settings in .env if needed
   ```

5. **Launch the application**
   ```bash
   docker-compose up --build
   ```

6. **Access the chatbot**
   - Open browser to `http://localhost:8501`
   - Start chatting!

## 💻 Usage

### Basic Chat

1. Navigate to `http://localhost:8501`
2. Type your message in the chat input
3. Press Enter to send
4. View AI responses in real-time

### Health Monitoring

- Click **"🔄 Check Health"** to verify service status
- Click **"🧪 Test Model"** to test direct API connectivity
- View statistics in the sidebar

### Management Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up --build

# Check service health
docker-compose ps
```

## 📁 Project Structure

```
Docker-LLM/
├── README.md                 # This file
├── .env                      # Environment configuration
├── docker-compose.yml        # Container orchestration
│
└── app/
    ├── Dockerfile           # Container definition
    ├── requirements.txt     # Python dependencies
    └── main.py             # Streamlit application
```

### Key Files

- **`docker-compose.yml`**: Orchestrates multi-container deployment
- **`app/Dockerfile`**: Defines Python runtime environment with health checks
- **`app/main.py`**: Main application logic with chat interface
- **`.env`**: Configuration for model, endpoints, and parameters

## 🎓 Technical Highlights

### Skills Demonstrated

#### DevOps & Infrastructure
- ✅ Docker containerization and multi-stage builds
- ✅ Docker Compose orchestration
- ✅ Container networking and service discovery
- ✅ Volume management for data persistence
- ✅ Health check implementation
- ✅ Environment-based configuration

#### Software Engineering
- ✅ Clean code architecture with separation of concerns
- ✅ Error handling and user feedback
- ✅ Session state management
- ✅ RESTful API integration
- ✅ Configuration management (12-factor methodology)

#### AI/ML Integration
- ✅ Local LLM deployment and inference
- ✅ OpenAI API compatibility layer
- ✅ Model quantization (Q4_K_M) for efficiency
- ✅ Conversation context management
- ✅ Temperature and token control


### Performance Optimizations

1. **Model Quantization**: Using Q4_K_M quantized model reduces memory usage by ~75%
2. **Container Caching**: Multi-stage Docker builds with layer caching
3. **Volume Persistence**: Model weights cached between container restarts
4. **Health Checks**: Automatic container recovery on failure

### Security Considerations

- No external API keys or credentials required
- All data processed locally
- Container isolation between services
- Environment variable based secrets management
- Non-root user execution in containers

## 🔮 Future Enhancements

### Planned Features

- [ ] **RAG Integration**: Document upload and retrieval-augmented generation
- [ ] **Multi-Model Support**: Switch between different LLMs
- [ ] **Conversation Export**: Save chat history to file
- [ ] **Authentication**: User authentication and session management
- [ ] **API Endpoints**: RESTful API for programmatic access
- [ ] **Monitoring**: Prometheus metrics and Grafana dashboards
- [ ] **Streaming Responses**: Real-time token streaming
- [ ] **Voice Input**: Speech-to-text integration

### Scalability Roadmap

- Kubernetes deployment manifests
- Load balancing for multiple replicas
- Database integration for persistent storage
- Redis caching layer
- CI/CD pipeline with GitHub Actions

## 📊 Performance Metrics

- **Startup Time**: < 30 seconds (with cached model)
- **Response Latency**: 2-5 seconds (depends on hardware)
- **Memory Usage**: ~2GB (model + runtime)
- **Container Size**: ~1.5GB (base image + dependencies)

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Connection error" in chat
- **Solution**: Verify Docker Model Runner is enabled and port 12434 is accessible
- **Check**: `curl http://localhost:12434/v1/models`

**Issue**: Container unhealthy
- **Solution**: Check logs with `docker-compose logs -f`
- **Verify**: Model is pulled with `docker model list`

**Issue**: Slow responses
- **Solution**: Reduce `MAX_TOKENS` in `.env` or use smaller model
- **Alternative**: Allocate more CPU/RAM to Docker Desktop

