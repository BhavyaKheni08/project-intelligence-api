import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

# Ensure env vars are loaded
load_dotenv()

def get_llm():
    """
    Factory function to get the LLM instance based on configuration.
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "ollama":
        model = os.getenv('OLLAMA_MODEL', 'llama3.2')
        base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
        print(f"🧠 Loading Ollama Model: {model} at {base_url}")
        return ChatOllama(
            model=model,
            base_url=base_url,
            temperature=0
        )
    else:
        print("🧠 Loading OpenAI Model")
        return ChatOpenAI(
            model="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0
        )
