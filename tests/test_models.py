from app.models import Employee


def test_employee_model():

    employee = Employee(
        id=1,
        name="Akash",
        department="Cloud",
        designation="DevOps",
        salary=85000
    )

    assert employee.id == 1

    assert employee.name == "Akash"

    assert employee.department == "Cloud"