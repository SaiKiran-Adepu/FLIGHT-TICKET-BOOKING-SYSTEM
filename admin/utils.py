from functools import wraps
from flask import session, redirect, url_for

def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if 'adm' not in session:  # Adjust 'adm' to your session variable for admin login
            return redirect(url_for('admin_login_bp.admin_login'))  # Adjust the blueprint and route for login
        return view_func(*args, **kwargs)
    return wrapped_view




