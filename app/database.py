from app.models import Employee

"""
Temporary in-memory database.

Later we will replace this with PostgreSQL
or Cloud SQL.

Keeping the API separate from the storage
allows easy migration.
"""

employees = [
    Employee(
        id=1,
        name="John Doe",
        department="IT",
        designation="Software Engineer",
        salary=65000,
    ),
    Employee(
        id=2,
        name="Jane Smith",
        department="HR",
        designation="HR Manager",
        salary=72000,
    ),
]