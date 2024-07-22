from flask import Blueprint
from .new_flight import new_flight_bp
from .add_airport import add_airport_bp
#from .airports import new_airport_bp #.file name and blue prints maked it in main folder to access any where while importing the code in routes.py where the html code contains
from .add_fare import add_fare_bp
from .ticket_admin import ticket_admin_bp 
from .ticket_admindb import ticket_admindb_bp 



admin_bp = Blueprint('admin', __name__)
# Register blueprints
admin_bp.register_blueprint(new_flight_bp)
admin_bp.register_blueprint(add_airport_bp)
admin_bp.register_blueprint(add_fare_bp)
admin_bp.register_blueprint(ticket_admin_bp)
admin_bp.register_blueprint(ticket_admindb_bp)

#admin_bp.register_blueprint(new_airport_bp) maked it in universersal

