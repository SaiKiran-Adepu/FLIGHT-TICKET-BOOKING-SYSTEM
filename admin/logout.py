from flask import Blueprint, redirect, url_for, session

admin_logout_bp = Blueprint('admin_logout_bp', __name__)

@admin_logout_bp.route('/admin/logout')
def admin_logout():
    # Clear session data
    session.clear()
    # Redirect to the home page or login page
    return redirect(url_for('home'))

