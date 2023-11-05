from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from classes import db, Accounts
from werkzeug.security import generate_password_hash, check_password_hash


account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = Accounts.query.filter_by(username=username).first()

        if not user:
            return jsonify({ "code": 401, "message": "No such account"}), 401 

        role = Roles.query.filter_by(id=user.role_id).first()

        if user and check_password_hash(user.password, password):
            token = create_access_token(identity={"username": user.username, "mcr": user.mcr, "role_name": role.role, "role_id": user.role_id})
            return jsonify({"code": 200, "token": token}), 200 

        return jsonify({ "code": 401, "message": "Incorrect username or password"}), 401
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@account_bp.route('/create_account', methods=['POST'])
def createAccount():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not mcr:
            mcr = None

        user = Accounts.query.filter_by(email=email).first()

        if user:
            return jsonify({"code": 409, "message": "User already exist"}), 409            
        
        password_hash = generate_password_hash(password)

        new_user = Accounts(
            username=username, 
            email=email,
            password=password_hash)
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify({ "code": 200, "message": "Success"}), 200 

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @account_bp.route('/editaccount', methods=['PUT'])
# def edit_account():
#     try:
#         data = request.get_json()
#         username = data.get('username')
#         new_name = data.get('newname')
#         new_role_id = data.get('newroleid')

#         user = Accounts.query.filter_by(username=username).first()

#         if not user:
#             return jsonify({ "code": 404, "message": "User does not exist."}), 404
        
#         if username == new_name and new_role_id == user.role_id:
#             return jsonify({ "code": 400, "message": "No changes were made."}), 400
        
#         if username != new_name:
#             setattr(user, 'username', new_name)
#         if new_role_id != user.role_id:
#             setattr(user, 'role_id', new_role_id)
        
#         db.session.commit()

#         return jsonify({"code": 200, "message": "User profile updated successfully"}), 200

#     except Exception as e:
#         return jsonify({"code": 500, 'message': str(e)}), 500
    
# @account_bp.route('/refresh/<username>', methods=['GET'])
# def refresh_token(username):
#     try:
#         user = Accounts.query.filter_by(username=username).first()

#         if not user:
#             return jsonify({ "code": 401, "message": "No such account"}), 401 

#         role = Roles.query.filter_by(id=user.role_id).first()
        
#         token = create_access_token(identity={"username": user.username, "mcr": user.mcr, "role_name": role.role, "role_id": user.role_id})
#         return jsonify({"code": 200, "token": token}), 200 
    
#     except Exception as e:
#         return jsonify({"code": 500, 'message': str(e)}), 500
    
# @account_bp.route('/users', methods=['GET'])
# def get_all_users():
#     users = Accounts.query.all()
#     users_list = [{'id': user.id, 'username': user.username, 'password': user.password, 'mcr': user.mcr, 'role_id': user.role_id} for user in users]
#     return jsonify({"code": 200, "data": users_list}), 200


# @account_bp.route('/update_user_role', methods=['PUT'])
# def update_user_role():
#     data = request.get_json()
#     user_id = data.get('id')
#     new_role_id = data.get('newUserRole')

#     user = Accounts.query.filter_by(id=user_id).first()
#     if user is None:
#         return jsonify({"error": "User not found"}), 404

#     setattr(user, 'role_id', new_role_id)
#     db.session.commit()

#     return jsonify({'id': user.id, 'role_id': user.role_id})