def validate_employee(data):
    """
    Validates the incoming employee payload.

    Returns:
        (True, "") if valid
        (False, error_message) otherwise.
    """

    required_fields = [
        "name",
        "department",
        "designation",
        "salary",
    ]

    for field in required_fields:

        if field not in data:

            return False, f"{field} is required"

    return True, ""