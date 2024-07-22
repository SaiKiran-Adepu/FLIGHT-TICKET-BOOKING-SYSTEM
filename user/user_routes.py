# user routes to hold .py files
from flask import Blueprint
from .ticket_user import ticket_user_bp 


user_bp = Blueprint('user', __name__)
# Register blueprints
user_bp.register_blueprint(ticket_user_bp)

