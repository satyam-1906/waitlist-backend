from sqlalchemy import create_engine, Integer, String, JSON
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column
import os
from dotenv import load_dotenv
from typing import Any, Dict

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL environment variable is required")
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class formData(Base):
    __tablename__ = 'waitlist'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    mobile_number: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    occupation: Mapped[str] = mapped_column(String)
    details: Mapped[Dict[str, Any]] = mapped_column(JSON)

Base.metadata.create_all(bind=engine)
