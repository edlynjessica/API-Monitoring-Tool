
from sqlalchemy import Column, ForeignKey, Integer, String
from src.database import Base


class Endpoint(Base):
    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    name = Column(String(100), nullable=False)
    url = Column(String, nullable=False)
