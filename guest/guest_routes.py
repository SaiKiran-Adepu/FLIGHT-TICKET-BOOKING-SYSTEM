from flask import Blueprint
from .user_register import user_register_bp
from .ticket_index import ticket_index_bp
from .feedback_index import feedback_index_bp

guest_bp = Blueprint('guest', __name__)

guest_bp.register_blueprint(user_register_bp)
guest_bp.register_blueprint(ticket_index_bp)
guest_bp.register_blueprint(feedback_index_bp)
