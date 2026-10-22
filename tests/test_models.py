
from sqlalchemy import inspect
from src.database import engine
from src.models.user import User
from src.models.endpoint import Endpoint
from src.models.check import Check


def test_tables_exist():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert "users" in tables
    assert "endpoints" in tables
    assert "checks" in tables


def test_model_table_names():
    assert User.__tablename__ == "users"
    assert Endpoint.__tablename__ == "endpoints"
    assert Check.__tablename__ == "checks"

def test_table_columns():
    inspector = inspect(engine)

    expected = {
        "users": {"id", "name", "email"},
        "endpoints": {"id", "user_id", "name", "url"},
        "checks": {
            "id",
            "endpoint_id",
            "status_code",
            "response_time_ms",
            "success",
            "checked_at",
        },
    }

    for table, expected_columns in expected.items():
        actual_columns = {
            column["name"]
            for column in inspector.get_columns(table)
        }

        assert actual_columns == expected_columns, (
            f"{table}: expected {expected_columns}, got {actual_columns}"
        )

    print("All database columns verified!")


if __name__ == "__main__":
    test_tables_exist()
    test_model_table_names()
    test_table_columns()

    print("All model checks passed!")