from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from agent import run_summarization_agent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Project Intelligence API",
    description="AI-powered API for intelligent project analytics and summarization",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from typing import Optional

class SummaryRequest(BaseModel):
    project_id: Optional[int] = None

class SummaryResponse(BaseModel):
    project_id: Optional[int] = None
    summary: dict

@app.get("/")
def read_root():
    """
    Root endpoint providing API information.
    """
    return {
        "message": "Welcome to the Project Intelligence API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "summarize": "POST /summarize"
        }
    }

@app.post("/summarize", response_model=SummaryResponse)
async def summarize_project(
    request: SummaryRequest, 
    db: Session = Depends(get_db)
):
    """
    Generate a comprehensive project summary from analytics data.
    
    This endpoint:
    1. Fetches project analytics data from external sources
    2. Processes the data using AI/LLM agents
    3. Returns a structured summary with executive summary, activity log, and action items
    
    **Request Body:**
    - `project_id` (optional): ID of the project to summarize
    
    **Response:**
    - `project_id`: The project ID (if provided)
    - `summary`: Structured summary object containing:
      - `project_name`: Name of the project
      - `executive_summary`: High-level summary paragraph
      - `activity_log`: Chronological list of activities
      - `pending_action_items`: List of pending tasks
    
    **Example Request:**
    ```json
    {
      "project_id": 123
    }
    ```
    
    **Example Response:**
    ```json
    {
      "project_id": 123,
      "summary": {
        "project_name": "Project Alpha",
        "executive_summary": "...",
        "activity_log": [...],
        "pending_action_items": [...]
      }
    }
    ```
    """
    try:
        summary = await run_summarization_agent()
        return SummaryResponse(project_id=request.project_id, summary=summary)
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to generate summary: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
