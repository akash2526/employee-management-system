from dataclasses import asdict

from flask import jsonify, request

from app.database import employees
from app.logger import logger
from app.models import Employee
from app.utils import validate_employee


def register_routes(app):
    """
    Register all API routes.
    """

    @app.route("/")
    def home():
        return jsonify({
            "application": "Employee Management System",
            "version": "1.0.0",
            "status": "Running"
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "Healthy"
        })

    @app.route("/employees", methods=["GET"])
    def get_employees():
        logger.info("Fetching all employees")

        return jsonify(
            [asdict(employee) for employee in employees]
        )

    @app.route("/employees/<int:employee_id>", methods=["GET"])
    def get_employee(employee_id):

        for employee in employees:

            if employee.id == employee_id:
                return jsonify(asdict(employee))

        return jsonify({
            "error": "Employee not found"
        }), 404

    @app.route("/employees", methods=["POST"])
    def create_employee():

        data = request.get_json()

        valid, message = validate_employee(data)

        if not valid:

            return jsonify({
                "error": message
            }), 400

        new_employee = Employee(
            id=len(employees) + 1,
            name=data["name"],
            department=data["department"],
            designation=data["designation"],
            salary=data["salary"]
        )

        employees.append(new_employee)

        logger.info(
            f"Employee created : {new_employee.name}"
        )

        return jsonify(
            asdict(new_employee)
        ), 201

    @app.route("/employees/<int:employee_id>", methods=["DELETE"])
    def delete_employee(employee_id):

        for employee in employees:

            if employee.id == employee_id:

                employees.remove(employee)

                logger.info(
                    f"Employee deleted : {employee.name}"
                )

                return jsonify({
                    "message": "Employee deleted successfully"
                })

        return jsonify({
            "error": "Employee not found"
        }), 404