from flask import Blueprint

from .ticket_admin import ticket_admin_bp 
from .seat_avl import seat_avl_bp

admin_bp = Blueprint('admin', __name__)

admin_bp.register_blueprint(ticket_admin_bp, url_prefix='/admin')#to book a ticket for search the airplanes
admin_bp.register_blueprint(seat_avl_bp, url_prefix='/admin')