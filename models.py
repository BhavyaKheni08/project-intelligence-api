from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    
    # Relationships
    microsurveys = relationship("Microsurvey", back_populates="project")

class Microsurvey(Base):
    __tablename__ = "microsurveys"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String)
    
    project = relationship("Project", back_populates="microsurveys")
    questions = relationship("MicrosurveyQuestion", back_populates="microsurvey")
    feeds = relationship("Feed", back_populates="microsurvey")

class MicrosurveyQuestion(Base):
    __tablename__ = "microsurvey_questions"
    id = Column(Integer, primary_key=True, index=True)
    microsurvey_id = Column(Integer, ForeignKey("microsurveys.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    
    microsurvey = relationship("Microsurvey", back_populates="questions")
    question = relationship("Question")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    
class Audience(Base):
    __tablename__ = "audiences"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feeds.id"))
    name = Column(String)

class Ranking(Base):
    __tablename__ = "rankings"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feeds.id"))
    rank = Column(Integer)

class QuestionStrength(Base):
    __tablename__ = "question_strengths"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    category = Column(String)

class Scale(Base):
    __tablename__ = "scales"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class QuestionScale(Base):
    __tablename__ = "question_scales"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    scale_id = Column(Integer, ForeignKey("scales.id"))

class Feed(Base):
    __tablename__ = "feeds"
    id = Column(Integer, primary_key=True, index=True)
    microsurvey_id = Column(Integer, ForeignKey("microsurveys.id"))
    customer_name = Column(String)
    
    microsurvey = relationship("Microsurvey", back_populates="feeds")
    answers = relationship("FeedQuestion", back_populates="feed")
    audiences = relationship("Audience", foreign_keys=[Audience.feed_id])
    rankings = relationship("Ranking", foreign_keys=[Ranking.feed_id])

class FeedQuestion(Base):
    __tablename__ = "feed_questions"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feeds.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer_text = Column(Text)
    
    feed = relationship("Feed", back_populates="answers")

class FeedQuestionScale(Base):
    __tablename__ = "feed_question_scales"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feeds.id"))
    score = Column(Float)

class Reason(Base):
    __tablename__ = "reasons"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feeds.id"))
    text = Column(Text)

class Recognition(Base):
    __tablename__ = "recognitions"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feeds.id"))
    text = Column(Text)

class Award(Base):
    __tablename__ = "awards"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feeds.id"))
    name = Column(String)
