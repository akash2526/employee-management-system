from dataclasses import dataclass

@dataclass
class Employee:
    """
    Represents a single employee.

    @dataclass automatically creates:
    - __init__()
    - __repr__()
    - __eq__()

    This reduces boilerplate code.
    """

    id: int
    name: str
    department: str
    designation: str
    salary: float