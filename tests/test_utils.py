from app.utils import validate_employee


def test_validate_employee_success():

    data = {
        "name": "Akash",
        "department": "Cloud",
        "designation": "DevOps",
        "salary": 85000
    }

    valid, message = validate_employee(data)

    assert valid is True

    assert message == ""


def test_validate_employee_failure():

    data = {
        "name": "Akash"
    }

    valid, message = validate_employee(data)

    assert valid is False