import time
import httpx

from sqlalchemy.orm import Session

from src.models.endpoint import Endpoint
from src.models.check import Check
from src.repositories import check_repository


def trigger_check(db: Session, endpoint: Endpoint) -> Check:

    start_time = time.perf_counter()

    try:
        response = httpx.get(
            endpoint.url,
            timeout=10.0
        )

        response_time = (time.perf_counter() - start_time) * 1000

        status_code = response.status_code
        success = 200 <= status_code < 300

    except httpx.RequestError:
        response_time = (time.perf_counter() - start_time) * 1000

        status_code = None
        success = False

    return check_repository.create_check(
        db=db,
        endpoint_id=endpoint.id,
        status_code=status_code,
        response_time_ms=response_time,
        success=success
    )