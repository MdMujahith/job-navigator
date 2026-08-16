from sqlalchemy import String,Integer,Sequence
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.database import Base

class Company(Base):

    __tablename__ = "companies"

    id:Mapped[int]=mapped_column(Integer, Sequence("networks_id_seq"), primary_key=True)
    name:Mapped[str]=mapped_column(String(255))
    website:Mapped[str]=mapped_column(String(255))
    location:Mapped[str | None ]=mapped_column(String(255))
    industry:Mapped[str]=mapped_column(String(255))