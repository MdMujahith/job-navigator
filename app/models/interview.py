from sqlalchemy import String, Text, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date
from app.database import Base

class Interview(Base):

    __tablename__ = "interviews"

    id:Mapped[int]=mapped_column(primary_key=True)
    job_id:Mapped[int]=mapped_column(ForeignKey("jobs.id"))
    title:Mapped[str]=mapped_column(String(255))
    status:Mapped[str]=mapped_column(String(255))
    stage:Mapped[str]=mapped_column(String(255))
    interview_schedule:Mapped[date|None]=mapped_column(Date)
    note:Mapped[str|None]=mapped_column(Text)