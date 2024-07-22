from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector

user_register_bp = Blueprint('user_register_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@user_register_bp.route('/guest/user_register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        try:
            # Get form data
            uname = request.form['username']
            passw = request.form['pass']  # Ensure unique usernames or handle duplicates
            gen = request.form['gen']
            address = request.form['addr']
            phone = request.form['phn']
            dob = request.form['dob']
            idt1 = request.form['idt']
            idn1 = request.form['idn']
            dor = request.form['dor']

            # Database operations
            con = get_db_connection()
            cursor = con.cursor()
            cursor.execute("SELECT user_no FROM airline_users WHERE dor = %s", (dor,))
            if cursor.fetchone():
                    error_message = 'User already exists.'
                    flash(error_message)
                    return redirect(url_for('guest.user_register_bp.user_register', error_message=error_message))

            # Insert user details
            insert_query = """
                INSERT INTO airline_users (USERNAME, PASSWORD, GENDER, ADDRESS, MOBILE_NUMBER, DOB, IDT, IDN, DOR)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (uname, passw, gen, address, phone, dob, idt1, idn1, dor))
            con.commit()

            if cursor.rowcount > 0:
                # Fetch user details
                select_query = """
                    SELECT *
                    FROM airline_users
                    WHERE username = %s AND dor = %s AND password = %s
                """
                cursor.execute(select_query, (uname, dor, passw))
                user_details = cursor.fetchall()

                cursor.close()
                con.close()

                return render_template('guest/register_success.html', user_details=user_details)
            else:
                cursor.close()
                con.close()
                error_message = 'Error occurred, please try again.'
                flash(error_message)
                return redirect(url_for('guest/user_register_bp.user_register'))

        except Exception as ex:
            print(ex)
            error_message = 'An error occurred during registration. Please try again.'
            flash(error_message)
            return redirect(url_for('user_register_bp.user_register'))
    
    return render_template('guest/user_register.html')


