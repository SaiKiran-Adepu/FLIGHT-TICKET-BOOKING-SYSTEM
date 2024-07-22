from flask import Blueprint, redirect, url_for, session

user_logout_bp = Blueprint('user_logout_bp', __name__)

@user_logout_bp.route('/user/logout')
def user_logout():
    # Clear session data
    session.clear()
    # Redirect to the home page or login page
    return redirect(url_for('home'))

