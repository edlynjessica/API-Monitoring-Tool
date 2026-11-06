from sqlalchemy.orm import Session

from src.models.check import Check

def create_check(
    db: Session,
    endpoint_id: int,
    status_code: int | None,
    response_time_ms: float | None,
    success: bool,
) -> Check:

    check = Check(
        endpoint_id=endpoint_id,
        status_code=status_code,
        response_time_ms=response_time_ms,
        success=success,
    )

    db.add(check)
    db.commit()
    db.refresh(check)

    return check

def get_checks_for_endpoint(
    db: Session,
    endpoint_id: int,
) -> list[Check]:

    return (
        db.query(Check)
        .filter(Check.endpoint_id == endpoint_id)
        .order_by(Check.checked_at.desc())
        .all()
    )

def get_check_by_id(
    db: Session,
    endpoint_id: int,
    check_id: int,
) -> Check | None:

    return (
        db.query(Check)
        .filter(
            Check.id == check_id,
            Check.endpoint_id == endpoint_id,
        )
        .first()
    )