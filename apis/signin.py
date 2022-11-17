from flask import Blueprint,request,jsonify
from models import *
from  werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token
signin_blueprint = Blueprint('signin',__name__,url_prefix='/api/v1/signin')

@signin_blueprint.route('/login',methods=['POST'])
def login():
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    user = User.query.filter_by(email=email).first()

    if user:
        is_pass_correct = check_password_hash(user.password, password)

        if is_pass_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            return ({"Message":f"Login successful {user.username} ",
                    "refresh": refresh,
                    "access": access})

    return jsonify({'error': 'Wrong credentials'})



