import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Application configuration settings.
    """
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dbname")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    # LLM Configuration
    # LLM Configuration
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "openai").lower()
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    # Config-driven data fetching: Table Name -> List of Columns to fetch
    # DATA_FETCH_CONFIG: dict = {
    #     "Task": ["title", "status", "priority"],
    #     "MeetingNote": ["content", "date"]
    # }

settings = Settings()
