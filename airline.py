from flask import Flask, render_template, redirect, url_for, session

from admin.admin_login import admin_login_bp
from admin.admin_routes import admin_bp # for python
from admin.routes import admin_dashboard_bp #importing Admin routes for html files
from admin.logout import admin_logout_bp  # Import the logout blueprint


from user.user_login import user_login_bp
from user.user_routes import user_bp
from user.routes import user_dashboard_bp  #for usesr .html files
from user.logout import user_logout_bp


from guest.routes import guest_dashboard_bp #for guest users in html html
from guest.guest_routes import guest_bp




app = Flask(__name__)
app.secret_key = 'SKA_AIRLINES_SAI KIRAN.'

# Register blueprints
#app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(admin_login_bp, url_prefix='/admin')
app.register_blueprint(admin_dashboard_bp, url_prefix='/admin')
# Uncomment and register other blueprints as needed
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(admin_logout_bp, url_prefix='/logout')

#user blue prints for user
app.register_blueprint(user_login_bp, url_prefix='/user')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(user_dashboard_bp, url_prefix='/user')
app.register_blueprint(user_logout_bp, url_prefix='/logout')

#blue prints for guest user like in index page
app.register_blueprint(guest_dashboard_bp, url_prefix='/guest')
app.register_blueprint(guest_bp, url_prefix='/guest')




@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/user')
#def user(): Dont call like this its out of the application sessions and diresctly accessing
#return render_template('user/welcome_user.html')

@app.route('/logout')
def logout():
    # Clear session data
    session.clear()
    # Redirect to the home page or login page
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
