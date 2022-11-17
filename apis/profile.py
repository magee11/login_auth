from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required
profile_blueprint = Blueprint('profile',__name__,url_prefix='/api/v1/profile')


@profile_blueprint.route('/profile',methods=['GET'])
@jwt_required()
def get_profile():

    return "Profile Page"