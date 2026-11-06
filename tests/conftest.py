import uuid
import pytest

from src.dependencies import get_db
from src.models.user import User
from src.models.endpoint import Endpoint


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
