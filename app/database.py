"""
Mock database for the Employee Management System.
In a real application, this would connect to MySQL, PostgreSQL, or another database.
"""

# Sample employee records
employees = [
    {
        "id": 1,
        "name": "John Doe",
        "department": "IT",
        "designation": "Software Engineer",
        "salary": 65000
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "department": "HR",
        "designation": "HR Manager",
        "salary": 72000
    }
]


def update_employee(employee_id, updated_data):
    """
    Update employee information.
    """

    for employee in employees:

        if employee["id"] == employee_id:

            employee.update(updated_data)

            return employee

    return None