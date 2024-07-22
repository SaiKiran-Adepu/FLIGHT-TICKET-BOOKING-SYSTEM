from flask import Blueprint, render_template, request, session, redirect, url_for
import mysql.connector

admin_login_bp = Blueprint('admin_login_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@admin_login_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        adname = request.form['namem']
        adpass = request.form['passm']

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM airline_Admins WHERE admin_name = %s AND admin_pass = %s"
        cursor.execute(query, (adname, adpass))
        admin = cursor.fetchone()

        cursor.close()
        conn.close()

        if admin:
            session['adm'] = adname
            #return redirect(url_for('admin_login_bp.welcome_admin', adname=adname))
            return redirect(url_for('admin_login_bp.welcome_admin'))#not display name on url good
        else:
            error_message = 'Invalid credentials. Please try again.'
            return render_template('adminlogin.html', error_message=error_message)

    return render_template('adminlogin.html')

@admin_login_bp.route('/welcome_admin')
def welcome_admin():
    adname = session.get('adm')
    if adname:
        return render_template('admin/welcome_admin.html', adname=adname)
    else:
        return redirect(url_for('admin_login_bp.admin_login'))
