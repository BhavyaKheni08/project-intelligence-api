# 🧠 Project Intelligence API

<div align="center">

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**AI-powered API for intelligent project analytics and summarization**

Transform raw project data into actionable insights with structured executive summaries, activity logs, and action items.

[Features](#-features) • [Quick Start](#-quick-start) • [API Documentation](#-api-documentation) • [Architecture](#-architecture)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

**Project Intelligence API** is a production-ready FastAPI service that leverages LangChain and Large Language Models (LLMs) to analyze project analytics data and generate comprehensive, structured summaries. Perfect for dashboard integrations, project management tools, and business intelligence applications.

### What It Does

- 🔍 **Analyzes** dashboard analytics data (sentiment analysis, action takers, reasons)
- 📊 **Generates** structured executive summaries
- 📝 **Creates** chronological activity logs
- ✅ **Identifies** pending action items
- 🎯 **Highlights** key insights and patterns

### Use Cases

- **Project Management**: Generate weekly/monthly project summaries
- **Business Intelligence**: Transform analytics data into executive reports
- **Dashboard Integration**: Add intelligent summarization to existing dashboards
- **Client Reporting**: Automatically generate client-facing project updates

## ✨ Features

- 🤖 **Multi-LLM Support**: Works with OpenAI GPT-4 and Ollama (local models)
- 🔄 **Flexible Architecture**: Easy to extend with custom data sources
- 📦 **Structured Output**: Pydantic models ensure consistent JSON responses
- 🚀 **FastAPI Powered**: High-performance async API with automatic documentation
- 🗄️ **Database Ready**: PostgreSQL integration with SQLAlchemy ORM
- 🔧 **Configurable**: Environment-based configuration for easy deployment
- 📚 **Well Documented**: Comprehensive API docs and code comments

## 🏗️ Architecture

```
┌─────────────────┐
│   FastAPI App   │
│   (main.py)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│  Agent Chain    │◄─────│  LangChain LLM   │
│  (agent.py)     │      │  (OpenAI/Ollama) │
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│  Data Service   │─────►│  External API    │
│ (data_service)  │      │  (Dashboard)     │
└─────────────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐
│  JSON Parser    │
│  (Pydantic)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Summary Report │
│  (Structured)   │
└─────────────────┘
```

### Data Flow

1. **Request** → FastAPI receives POST request to `/summarize`
2. **Data Fetch** → `data_service.py` fetches analytics data from external API
3. **Processing** → LangChain agent processes data with LLM
4. **Parsing** → JSON output parser structures the response
5. **Response** → Returns structured summary report

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- PostgreSQL (optional, for database features)
- OpenAI API key OR Ollama installed locally

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/project-intelligence-api.git
   cd project-intelligence-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access API documentation**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 📡 API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

#### `GET /`

Welcome endpoint that returns API information.

**Response:**
```json
{
  "message": "Welcome to the AI Summary Agent API"
}
```

#### `POST /summarize`

Generate a project summary from analytics data.

**Request Body:**
```json
{
  "project_id": 123  // Optional
}
```

**Response:**
```json
{
  "project_id": 123,
  "summary": {
    "project_name": "Project Alpha",
    "executive_summary": "The project is on track with key milestones met...",
    "activity_log": [
      {
        "date": "2023-10-01",
        "description": "Initial Setup and Environment Configuration",
        "category": "Planning"
      }
    ],
    "pending_action_items": [
      "Complete API Endpoints",
      "Finalize Documentation"
    ]
  }
}
```

**cURL Example:**
```bash
curl -X POST "http://localhost:8000/summarize" \
  -H "Content-Type: application/json" \
  -d '{"project_id": 123}'
```

**Python Example:**
```python
import requests

response = requests.post(
    "http://localhost:8000/summarize",
    json={"project_id": 123}
)
print(response.json())
```

### Response Schema

```python
{
  "project_id": int | None,
  "summary": {
    "project_name": str,
    "executive_summary": str,
    "activity_log": [
      {
        "date": str,
        "description": str,
        "category": str
      }
    ],
    "pending_action_items": [str]
  }
}
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Database Configuration (Optional)
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# LLM Provider: "openai" or "ollama"
LLM_PROVIDER=openai

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Ollama Configuration (if using Ollama)
OLLAMA_MODEL=llama3.2
OLLAMA_BASE_URL=http://localhost:11434
```

### LLM Providers

#### OpenAI (Default)
- Requires: `OPENAI_API_KEY`
- Model: GPT-4o
- Best for: Production use, highest quality

#### Ollama (Local)
- Requires: Ollama installed locally
- Model: Configurable (default: llama3.2)
- Best for: Privacy, cost savings, offline use

## 📁 Project Structure

```
project-intelligence-api/
├── main.py                 # FastAPI application entry point
├── agent.py                # LangChain agent and summarization logic
├── config.py               # Configuration settings
├── database.py             # Database connection and session management
├── data_service.py         # External API data fetching
├── models.py               # SQLAlchemy database models
├── seed_db.py             # Database seeding script
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── README.md              # This file
├── database_metadata.md   # Database schema documentation
└── utils/
    └── llm_factory.py     # LLM provider factory
```

### Key Files Explained

- **`main.py`**: FastAPI app with route definitions
- **`agent.py`**: Core summarization logic using LangChain
- **`data_service.py`**: Fetches data from external dashboard API
- **`config.py`**: Centralized configuration management
- **`utils/llm_factory.py`**: Factory pattern for LLM provider selection

## 🔧 Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### Code Style

This project follows PEP 8 style guidelines. Use `black` for formatting:

```bash
pip install black
black .
```

### Database Setup

If using PostgreSQL:

```bash
# Create database
createdb project_intelligence

# Run migrations (if using Alembic)
alembic upgrade head

# Seed database (optional)
python seed_db.py
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

1. Fork and clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Install dev dependencies: `pip install -r requirements-dev.txt` (if exists)
5. Create `.env` file from `.env.example`
6. Make your changes
7. Run tests and linting
8. Submit a PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [LangChain](https://www.langchain.com/) for LLM orchestration
- [OpenAI](https://openai.com/) and [Ollama](https://ollama.ai/) for LLM providers

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

<div align="center">

Made with ❤️ by [Your Name]

⭐ Star this repo if you find it helpful!

</div>
