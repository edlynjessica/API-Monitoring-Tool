
from sqlalchemy.orm import Session
    
from src.models.endpoint import Endpoint


def create_endpoint(
    db: Session,
    user_id: int,
    name: str,
    url: str,
) -> Endpoint:
    endpoint = Endpoint(
        user_id=user_id,
        name=name,
        url=url,
    )

    db.add(endpoint)
    db.commit()
    db.refresh(endpoint)

    return endpoint


def get_all_endpoints(db: Session, user_id: int) -> list[Endpoint]:
    return (
        db.query(Endpoint)
        .filter(Endpoint.user_id == user_id)
        .all()
    )


def get_endpoint_by_id(
    db: Session,
    endpoint_id: int,
    user_id: int,
) -> Endpoint | None:
    return (
        db.query(Endpoint)
        .filter(
            Endpoint.id == endpoint_id,
            Endpoint.user_id == user_id,
        )
        .first()
    )


def delete_endpoint(db: Session, endpoint: Endpoint) -> None:
    db.delete(endpoint)
    db.commit()
