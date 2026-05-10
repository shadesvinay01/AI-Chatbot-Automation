from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///baatai.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    business_name = Column(String)
    whatsapp_number = Column(String, unique=True)
    knowledge_base = Column(JSON)      # Store documents text
    flows = Column(JSON)               # Custom flows
    created_at = Column(String)

# Create tables
Base.metadata.create_all(engine)
