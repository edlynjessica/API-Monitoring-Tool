from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.schemas.check import CheckResponse
from src.repositories import endpoint_repository, check_repository
from src.services import monitoring_service


router = APIRouter(
    prefix="/endpoints",
    tags=["Checks"]
)

DEFAULT_USER_ID = 80


@router.post(
    "/{endpoint_id}/checks",
    response_model=CheckResponse,
    status_code=status.HTTP_201_CREATED
)
def trigger_check(
    endpoint_id: int,
    db: Session = Depends(get_db)
):
    endpoint = endpoint_repository.get_endpoint_by_id(
        db=db,
        endpoint_id=endpoint_id,
        user_id=DEFAULT_USER_ID
    )

    if endpoint is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Endpoint not found"
        )

    return monitoring_service.trigger_check(db, endpoint)


@router.get(
    "/{endpoint_id}/checks",
    response_model=list[CheckResponse]
)
def get_check_history(
    endpoint_id: int,
    db: Session = Depends(get_db)
):
    endpoint = endpoint_repository.get_endpoint_by_id(
        db=db,
        endpoint_id=endpoint_id,
        user_id=DEFAULT_USER_ID
    )

    if endpoint is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Endpoint not found"
        )

    return check_repository.get_checks_for_endpoint(
        db=db,
        endpoint_id=endpoint_id
    )


@router.get(
    "/{endpoint_id}/checks/{check_id}",
    response_model=CheckResponse
)
def get_check(
    endpoint_id: int,
    check_id: int,
    db: Session = Depends(get_db)
):
    endpoint = endpoint_repository.get_endpoint_by_id(
        db=db,
        endpoint_id=endpoint_id,
        user_id=DEFAULT_USER_ID
    )

    if endpoint is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Endpoint not found"
        )

    check = check_repository.get_check_by_id(
        db=db,
        endpoint_id=endpoint_id,
        check_id=check_id
    )

    if check is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Check not found"
        )

    return check