from sqlalchemy import String, Text, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date
from app.database import Base

class Job(Base):

    __tablename__ = "jobs"

    id:Mapped[int]=mapped_column(primary_key=True)
    company_id:Mapped[int]=mapped_column(ForeignKey("companies.id"))
    title:Mapped[str]=mapped_column(String(255))
    description:Mapped[str|None]=mapped_column(Text)
    posted_date:Mapped[date|None]=mapped_column(Date)
    salary:Mapped[float]=mapped_column()
    apply_link:Mapped[str]=mapped_column(String(255))
