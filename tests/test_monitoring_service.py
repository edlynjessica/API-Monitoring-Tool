from unittest.mock import patch, Mock

import httpx
import pytest

from src.dependencies import get_db
from src.services import monitoring_service


def test_trigger_check_success(db, test_endpoint):
    mock_response = Mock()
    mock_response.status_code = 200

    with patch(
        "src.services.monitoring_service.httpx.get",
        return_value=mock_response
    ):
        check = monitoring_service.trigger_check(db, test_endpoint)

    assert check.status_code == 200
    assert check.success is True
    assert check.response_time_ms >= 0


def test_trigger_check_http_error(db, test_endpoint):
    mock_response = Mock()
    mock_response.status_code = 500

    with patch(
        "src.services.monitoring_service.httpx.get",
        return_value=mock_response
    ):
        check = monitoring_service.trigger_check(db, test_endpoint)

    assert check.status_code == 500
    assert check.success is False


def test_trigger_check_network_failure(db, test_endpoint):
    with patch(
        "src.services.monitoring_service.httpx.get",
        side_effect=httpx.ConnectError("Connection failed")
    ):
        check = monitoring_service.trigger_check(db, test_endpoint)

    assert check.status_code is None
    assert check.success is False
    assert check.response_time_ms >= 0