"""
Application Routes
------------------
This file contains all API endpoints for the Employee Management System.
"""

from flask import jsonify, request

from app.database import employees, update_employee
from app.utils import validate_employee


def register_routes(app):
    """
    Register all application routes.
    """

    # ==========================================================
    # Home API
    # ==========================================================

    @app.route("/")
    def home():
        """
        Home endpoint.
        """

        return jsonify({
            "application": "Employee Management System",
            "version": "1.0",
            "status": "Running"
        })

    # ==========================================================
    # Health Check API
    # ==========================================================

    @app.route("/health")
    def health():
        """
        Health endpoint.
        """

        return jsonify({
            "status": "Healthy"
        })

    # ==========================================================
    # Get Employees
    # ==========================================================

    @app.route("/employees", methods=["GET"])
    def get_employees():
        """
        Return all employees.
        """

        return jsonify(employees)

    # ==========================================================
    # Add Employee
    # ==========================================================

    @app.route("/employees", methods=["POST"])
    def add_employee():
        """
        Add a new employee.
        """

        employee = request.get_json()

        if not validate_employee(employee):
            return jsonify({
                "message": "Invalid Employee Data"
            }), 400

        employees.append(employee)

        return jsonify({
            "message": "Employee added successfully",
            "employee": employee
        }), 201

    # ==========================================================
    # Update Employee
    # ==========================================================

    @app.route("/employees/<int:employee_id>", methods=["PUT"])
    def update_employee_route(employee_id):
        """
        Update employee details.
        """

        updated_data = request.get_json()

        employee = update_employee(employee_id, updated_data)

        if employee:

            return jsonify({
                "message": "Employee updated successfully",
                "employee": employee
            }), 200

        return jsonify({
            "message": "Employee not found"
        }), 404

    # ==========================================================
    # Delete Employee
    # ==========================================================

    @app.route("/employees/<int:employee_id>", methods=["DELETE"])
    def delete_employee(employee_id):
        """
        Delete employee.
        """

        for employee in employees:

            if employee["id"] == employee_id:

                employees.remove(employee)

                return jsonify({
                    "message": "Employee deleted successfully"
                }), 200

        return jsonify({
            "message": "Employee not found"
        }), 404