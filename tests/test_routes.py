import pytest

from app.app import app


@pytest.fixture
def client():
    """
    Creates a Flask test client.
    """
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    """
    Test home endpoint.
    """

    response = client.get("/")

    assert response.status_code == 200

    json_data = response.get_json()

    assert json_data["application"] == "Employee Management System"


def test_health(client):
    """
    Test health endpoint.
    """

    response = client.get("/health")

    assert response.status_code == 200

    assert response.get_json()["status"] == "Healthy"


def test_get_employees(client):
    """
    Test GET /employees
    """

    response = client.get("/employees")

    assert response.status_code == 200

    assert isinstance(response.get_json(), list)