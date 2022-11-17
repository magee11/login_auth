from flask import Blueprint,request,jsonify
from models import *
from  werkzeug.security import generate_password_hash
from flask_mail import Message
import traceback

signup_blueprint = Blueprint('signup',__name__,url_prefix='/api/v1/signup')

@signup_blueprint.route('/register',methods=['POST'])
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is taken"}) 

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': "username is taken"})

    pwd_hash = generate_password_hash(password)

    user = User(username=username, password=pwd_hash, email=email)
    db.session.add(user)
    db.session.commit()

    return "Added user"

@signup_blueprint.route('/mail',methods=['GET'])
def mail():
    try:
            msg = Message(
            'Hello',
            sender='magesh@divum.in',
            recipients=['mageshmarch@gmail.com']
            )
            msg.body = "Hey! this is mail from flask_mail to check ths is working properly"
            msg.send(msg)
            return 'Sent'
    except Exception as e:
        print(traceback.format_exc)
        return(traceback.format_list)
