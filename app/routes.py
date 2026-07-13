from flask import jsonify

def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "application": "Employee Management System",
            "status": "Running"
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "Healthy"
        })