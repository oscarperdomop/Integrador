from flask import request, jsonify
from .models import User

def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user:
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'User not found!'}), 404
