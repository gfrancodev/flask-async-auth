from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__, url_prefix='/v1/auth')

@auth.route("/register", methods=["POST"])
async def register():
    return jsonify({"message": "Registro Ok!"})

@auth.route("/login", methods=["POST"])
async def login():
    return jsonify({"message": "Login Ok!"})

@auth.route("/forgot_password", methods=["POST"])
async def forgot_password():
    return jsonify({"message": "Forgot Password Ok!"})

@auth.route("/reset/password", methods=["POST"])
async def reset_password():
    return jsonify({"message": "Reset Password Ok!"})

@auth.route("/request/confirm_email", methods=["POST"])
async def request_confirm_email():
    return jsonify({"message": "Reques Confirm E-mail Ok!"})

@auth.route("/confirm/email", methods=["POST"])
async def confirm_email():
    return jsonify({"message": "Confirm E-mail Ok!"})