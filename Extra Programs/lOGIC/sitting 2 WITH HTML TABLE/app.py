from flask import Flask
from seat_availability import seat_avl_bp  # Import your actual blueprint

app = Flask(__name__)

# Register the existing blueprint
app.register_blueprint(seat_avl_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
#http://localhost:5000/admin/seat_avl