from flask import Blueprint, render_template, request, session, redirect, url_for
import mysql.connector

user_login_bp = Blueprint('user_login_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@user_login_bp.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        unumber = request.form['number']
        uname = request.form['name']
        upass = request.form['passc']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airline_users WHERE user_no = %s AND username = %s AND password = %s"
        cursor.execute(query, (unumber, uname, upass))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session['unumber'] = unumber
            session['uname'] = uname
            session.permanent = True  # Make the session permanent
            #return redirect(url_for('user_login_bp.welcome_user', uname=uname)) its display user name on url
            return redirect(url_for('user_login_bp.welcome_user'))# but its not display user namr on url good
        else:
            error_message = 'Invalid credentials. Please try again.'
            return render_template('userlogin.html', error_message=error_message)

    return render_template('userlogin.html')

@user_login_bp.route('/welcome_user')
def welcome_user():
    unumber, uname = session.get('unumber'), session.get('uname')
    if unumber:
     return render_template('user/welcome_user.html', unumber=unumber, uname=uname)
    else:
     return redirect(url_for('user_login_bp.user_login'))
