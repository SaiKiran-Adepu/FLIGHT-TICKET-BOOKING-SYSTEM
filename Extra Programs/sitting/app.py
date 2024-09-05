from flask import Flask, render_template
from admin.seat_avl import seat_avl_bp  # Import your actual blueprint
from admin.routes import admin_dashboard_bp #importing Admin routes for html files
from admin.admin_routes import admin_bp # for python

app = Flask(__name__)
app.secret_key = 'SKA_AIRLINES_SAI KIRAN.'

# Register the existing blueprint
app.register_blueprint(seat_avl_bp, url_prefix='')

app.register_blueprint(admin_dashboard_bp, url_prefix='/admin')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
#http://localhost:5000/admin/seat_avl