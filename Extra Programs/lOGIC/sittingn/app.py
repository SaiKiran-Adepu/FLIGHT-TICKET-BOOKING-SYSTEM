from flask import Flask
from admin.seat_avl import seat_avl_bp  # Import your actual blueprint

app = Flask(__name__)

# Register the existing blueprint
app.register_blueprint(seat_avl_bp, url_prefix='')

if __name__ == '__main__':
    app.run(debug=True)
#http://localhost:5000/admin/seat_avl