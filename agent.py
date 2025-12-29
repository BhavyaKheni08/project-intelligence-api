from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda
import re
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from config import settings
import json

# --- Output Schema ---
class ActivityLogItem(BaseModel):
    date: str = Field(description="Date of the activity or N/A")
    description: str = Field(description="Formal description of the task or note, void of technical jargon")
    category: str = Field(description="e.g., 'Planning', 'Development', 'Review'")

class SummaryReport(BaseModel):
    project_name: str
    executive_summary: str = Field(description="A high-level, formal paragraph summarizing the project's current state for a client.")
    activity_log: List[ActivityLogItem] = Field(description="Detailed chronological log of all completed tasks and notes.")
    pending_action_items: List[str] = Field(description="List of tasks that are currently open or in progress.")

# --- One-Shot Example ---
EXAMPLE_JSON = json.dumps({
  "project_name": "Project Alpha",
  "executive_summary": "The project is on track with key milestones met. The development team has resolved initial database connectivity issues and is currently focusing on API implementation.",
  "activity_log": [
    {"date": "2023-10-01", "description": "Initial Setup and Environment Configuration", "category": "Planning"},
    {"date": "2023-10-02", "description": "Resolved Database Connectivity Issues", "category": "Development"}
  ],
  "pending_action_items": ["Complete API Endpoints", "Finalize Documentation"]
}, indent=2)

from data_service import fetch_dashboard_context

# --- Prompt Template ---
PROMPT_TEMPLATE = """You are analyzing the Close Loop Analytics Dashboard. The data is organized by 'Sentiment' (Positive, Neutral, Negative) and 'Category' (Analytics, Reasons, Action Takers). Identify the main drivers for negative feedback and highlight who is taking the most action.

OUTPUT FORMAT:
You must strictly follow this structure.
Do not return the schema definition. Return an actual instance.

EXAMPLE OUTPUT:
{example_json}

YOUR TASK:
Context: {context_data}

Return ONLY the JSON.
"""

from utils.llm_factory import get_llm

def clean_json_output(ai_message):
    """
    Cleans the LLM output to ensure clean JSON string is passed to the parser.
    """
    text = ai_message.content if hasattr(ai_message, 'content') else str(ai_message)
    cleaned = re.sub(r"```json\s*", "", text)
    cleaned = re.sub(r"```", "", cleaned)
    return cleaned.strip()

def get_agent_chain():
    """
    Constructs and returns the LangChain agent chain.
    """
    try:
        llm = get_llm()
    except Exception as e:
        # Fallback if get_llm fails or prints error
        print(f"Error initializing LLM: {e}")
        raise e

    parser = JsonOutputParser()

    prompt = PromptTemplate(
        input_variables=["context_data", "example_json"],
        template=PROMPT_TEMPLATE,
    )

    chain = prompt | llm | RunnableLambda(clean_json_output) | parser
    
    return chain

async def run_summarization_agent() -> dict:
    """
    Runs the agent to summarize the provided project context.
    """
    # 1. Fetch Context via Dashboard API
    context_data = fetch_dashboard_context()
    
    chain = get_agent_chain()
    
    try:
        response_obj = chain.invoke({
            "context_data": context_data,
            "example_json": EXAMPLE_JSON
        })
        return response_obj
    except Exception as e:
        return {"error": f"Failed to generate summary: {str(e)}"}
