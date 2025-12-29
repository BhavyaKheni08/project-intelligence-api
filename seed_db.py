import logging
import datetime
from database import engine, SessionLocal, Base
from models import Project, Task, MeetingNote

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed():
    """
    Drops existing tables, creates new ones, and seeds the database with sample data.
    """
    logger.info("Dropping existing tables...")
    Base.metadata.drop_all(bind=engine)
    
    logger.info("Creating tables...")
    Base.metadata.create_all(bind=engine)
    
    session = SessionLocal()
    try:
        logger.info("Seeding data...")
        
        # Create a Project
        project = Project(
            name="AI Agent MVP",
            description="Building a minimum viable product for the AI summary agent.",
            owner="Alice"
        )
        session.add(project)
        session.commit() # Commit to generate ID
        session.refresh(project)
        
        # Create Tasks
        task1 = Task(
            title="Setup FastAPI structure",
            status="Done",
            priority="High",
            project_id=project.id
        )
        task2 = Task(
            title="Implement LangChain integration",
            status="In Progress",
            priority="High",
            project_id=project.id
        )
        task3 = Task(
            title="Write documentation",
            status="Pending",
            priority="Low",
            project_id=project.id
        )
        
        # Create Meeting Notes
        note1 = MeetingNote(
            content="Kickoff meeting: Discussed scope and timeline. Agreed on Python 3.10+.",
            date=datetime.datetime.utcnow() - datetime.timedelta(days=2),
            project_id=project.id
        )
        note2 = MeetingNote(
            content="Sync: Blocked on DB credentials, resolved after call.",
            date=datetime.datetime.utcnow(),
            project_id=project.id
        )
        
        session.add_all([task1, task2, task3, note1, note2])
        session.commit()
        
        logger.info(f"Database seeded successfully! Created Project ID: {project.id}")
        
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    seed()
