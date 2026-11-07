from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.schemas.endpoint import EndpointCreate, EndpointResponse
from src.repositories import endpoint_repository


router = APIRouter(
    prefix="/endpoints",
    tags=["Endpoints"]
)

DEFAULT_USER_ID = 80


@router.post(
    "/",
    response_model=EndpointResponse,
    status_code=status.HTTP_201_CREATED
)
def create_endpoint(
    endpoint_data: EndpointCreate,
    db: Session = Depends(get_db)
):
    return endpoint_repository.create_endpoint(
        db=db,
        user_id=DEFAULT_USER_ID,
        name=endpoint_data.name,
        url=endpoint_data.url
    )


@router.get("/", response_model=list[EndpointResponse])
def get_all_endpoints(
    db: Session = Depends(get_db)
):
    return endpoint_repository.get_all_endpoints(
        db=db,
        user_id=DEFAULT_USER_ID
    )


@router.get("/{endpoint_id}", response_model=EndpointResponse)
def get_endpoint(
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

    return endpoint


@router.delete(
    "/{endpoint_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_endpoint(
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

    endpoint_repository.delete_endpoint(db, endpoint)