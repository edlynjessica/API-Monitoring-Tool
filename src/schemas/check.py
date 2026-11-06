from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CheckResponse(BaseModel):
    id: int
    endpoint_id: int
    status_code: int | None
    response_time_ms: Decimal | None
    success: bool
    checked_at: datetime

    model_config = ConfigDict(from_attributes=True)
    # Lets Pydantic serialize SQLAlchemy model objects.