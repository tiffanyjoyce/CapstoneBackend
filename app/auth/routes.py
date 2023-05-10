from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash
from flask_login import logout_user, login_user, current_user

from ..models import User

auth = Blueprint('auth', __name__)

@auth.post('/signup')
def registerPage():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 409
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'email already used'}), 409
    
    user = User(username=username,email=email,password=password)
    user.saveUser()

    session ['user_id'] = user.id

    print(f"Welcome, {user.username}")
    return jsonify({
        'id':user.id,
        'email': user.email,
        'username':user.username
    })

@auth.post('/login')
def loginPage():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        if user.password==password:

            session['user_id']= user.id

            return jsonify({'id':user.id, 'username': user.username})

        else:
            return jsonify({'error': 'wrong password'}), 401

    else:
        return jsonify({'error': 'this user does not exist'}), 401
    
@auth.route('/@me')
def get_current_user():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify ({'error':'Unauthorized'}), 401
    
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        'id': user.id,
        'username': user.username
    })