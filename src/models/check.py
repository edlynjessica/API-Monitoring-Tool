
from sqlalchemy import (
    Column,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    text,
)
from src.database import Base


class Check(Base):
    __tablename__ = "checks"

    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(
        Integer,
        ForeignKey("endpoints.id", ondelete="CASCADE"),
        nullable=False
    )
    status_code = Column(Integer, nullable=True)
    response_time_ms = Column(Numeric(10, 2), nullable=True)
    success = Column(Boolean, nullable=False)
    checked_at = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
