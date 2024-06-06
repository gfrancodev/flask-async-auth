from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__, url_prefix='/v1/auth')

@auth.route("/register", methods=["POST"])
def register():
    return jsonify({"message": "Registro Ok!"})

@auth.route("/login", methods=["POST"])
def login():
    return jsonify({"message": "Login Ok!"})

@auth.route("/forgot_password", methods=["POST"])
def forgot_password():
    return jsonify({"message": "Forgot Password Ok!"})

@auth.route("/reset/password", methods=["POST"])
def reset_password():
    return jsonify({"message": "Reset Password Ok!"})

@auth.route("/request/confirm_email", methods=["POST"])
def request_confirm_email():
    return jsonify({"message": "Reques Confirm E-mail Ok!"})

@auth.route("/confirm/email", methods=["POST"])
def confirm_email():
    return jsonify({"message": "Confirm E-mail Ok!"})