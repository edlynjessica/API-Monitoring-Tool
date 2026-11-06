
import uuid
import pytest

from src.database import SessionLocal
from src.models.user import User
from src.models.endpoint import Endpoint
from src.repositories import endpoint_repository
from src.dependencies import get_db

@pytest.fixture
def db():
    db_generator = get_db()
    db = next(db_generator)

    try:
        yield db
    finally:
        db_generator.close()

@pytest.fixture
def test_user(db):
    user = User(
        name="Test User",
        email=f"test_{uuid.uuid4().hex}@example.com"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    yield user

    db.delete(user)
    db.commit()


@pytest.fixture
def another_user(db):
    user = User(
        name="Another User",
        email=f"another_{uuid.uuid4().hex}@example.com"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    yield user

    db.delete(user)
    db.commit()


def test_create_endpoint(db, test_user):
    endpoint = endpoint_repository.create_endpoint(
        db,
        test_user.id,
        "Test API",
        "https://example.com"
    )

    assert endpoint.id is not None
    assert endpoint.user_id == test_user.id
    assert endpoint.name == "Test API"
    assert endpoint.url == "https://example.com"


def test_get_all_endpoints(db, test_user, another_user):
    endpoint_repository.create_endpoint(
        db, test_user.id, "API 1", "https://api1.com"
    )
    endpoint_repository.create_endpoint(
        db, test_user.id, "API 2", "https://api2.com"
    )
    endpoint_repository.create_endpoint(
        db, another_user.id, "Other API", "https://other.com"
    )

    endpoints = endpoint_repository.get_all_endpoints(
        db, test_user.id
    )

    assert len(endpoints) == 2
    assert all(e.user_id == test_user.id for e in endpoints)


def test_get_endpoint_by_id(db, test_user):
    created = endpoint_repository.create_endpoint(
        db, test_user.id, "Test API", "https://example.com"
    )

    endpoint = endpoint_repository.get_endpoint_by_id(
        db, created.id, test_user.id
    )

    assert endpoint is not None
    assert endpoint.id == created.id


def test_get_endpoint_by_id_not_found(db, test_user, another_user):
    created = endpoint_repository.create_endpoint(
        db, test_user.id, "Test API", "https://example.com"
    )

    # Another user must not be able to retrieve this endpoint.
    endpoint = endpoint_repository.get_endpoint_by_id(
        db, created.id, another_user.id
    )

    assert endpoint is None

    # A nonexistent ID should also return None.
    missing = endpoint_repository.get_endpoint_by_id(
        db, -1, test_user.id
    )

    assert missing is None


def test_delete_endpoint(db, test_user):
    created = endpoint_repository.create_endpoint(
        db, test_user.id, "Test API", "https://example.com"
    )

    endpoint_repository.delete_endpoint(db, created)

    deleted = endpoint_repository.get_endpoint_by_id(
        db, created.id, test_user.id
    )

    assert deleted is None
