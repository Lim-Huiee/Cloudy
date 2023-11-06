from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from classes import db, Accounts
from werkzeug.security import generate_password_hash, check_password_hash


accounts_bp = Blueprint('accounts_bp', __name__)

@accounts_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = Accounts.query.filter_by(email=email).first()

        if not user:
            return jsonify({ "code": 401, "message": "No such account"}), 401 

        if user and check_password_hash(user.password, password):
            return jsonify({"code": 200, "email": email}), 200 

        return jsonify({ "code": 401, "message": "incorrect email or password"}), 401
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@accounts_bp.route('/create_account', methods=['POST'])
def createAccount():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = Accounts.query.filter_by(email=email).first()

        if user:
            return jsonify({"code": 409, "message": "User already exist"}), 409            
        
        password_hash = generate_password_hash(password, "sha256")

        new_user = Accounts(
            username=username, 
            email=email,
            password=password_hash)
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify({ "code": 200, "message": "Success"}), 200 

    except Exception as e:
        return jsonify({'error': str(e)}), 500