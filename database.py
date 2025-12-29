from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# Create SQLAlchemy engine
# connect_args={"check_same_thread": False} is needed only for SQLite. required for PostgreSQL? No.
engine = create_engine(settings.DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_db():
    """
    Dependency that provides a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def fetch_project_data(project_id: int) -> str:
    """
    Placeholder function to fetch project data.
    
    Args:
        project_id (int): The ID of the project to fetch.
        
    Returns:
        str: Dummy text for now.
    """
    # In the future, this will query the database using the project_id
    # e.g., project = db.query(Project).filter(Project.id == project_id).first()
    return f"Dummy data for project {project_id}. This is content to be summarized."
