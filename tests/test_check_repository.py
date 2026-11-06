import uuid
import pytest

from src.models.user import User
from src.models.endpoint import Endpoint
from src.dependencies import get_db
from src.repositories import check_repository


@pytest.fixture
def db():
    db_generator = get_db()
    db = next(db_generator)
    try:
        yield db
    finally:
        db_generator.close()


@pytest.fixture
def test_endpoint(db):
    user = User(
        name="Test User",
        email=f"{uuid.uuid4()}@test.com"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    endpoint = Endpoint(
        user_id=user.id,
        name="Test API",
        url="https://example.com"
    )
    db.add(endpoint)
    db.commit()
    db.refresh(endpoint)

    yield endpoint

    db.delete(user)
    db.commit()


def test_create_check(db, test_endpoint):
    check = check_repository.create_check(
        db=db,
        endpoint_id=test_endpoint.id,
        status_code=200,
        response_time_ms=142.50,
        success=True
    )

    assert check.id is not None
    assert check.endpoint_id == test_endpoint.id
    assert check.status_code == 200
    assert float(check.response_time_ms) == 142.50
    assert check.success is True
    assert check.checked_at is not None


def test_get_checks_for_endpoint(db, test_endpoint):
    check_repository.create_check(
        db, test_endpoint.id, 200, 100.0, True
    )
    check_repository.create_check(
        db, test_endpoint.id, 503, 200.0, False
    )

    checks = check_repository.get_checks_for_endpoint(
        db, test_endpoint.id
    )

    assert len(checks) == 2
    assert checks[0].checked_at >= checks[1].checked_at


def test_get_check_by_id(db, test_endpoint):
    created = check_repository.create_check(
        db, test_endpoint.id, 200, 150.0, True
    )

    result = check_repository.get_check_by_id(
        db, test_endpoint.id, created.id
    )

    assert result is not None
    assert result.id == created.id


def test_get_check_by_id_wrong_endpoint(db, test_endpoint):
    created = check_repository.create_check(
        db, test_endpoint.id, 200, 150.0, True
    )

    result = check_repository.get_check_by_id(
        db, endpoint_id=999999, check_id=created.id
    )

    assert result is None