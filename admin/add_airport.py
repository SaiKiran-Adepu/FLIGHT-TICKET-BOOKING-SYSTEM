from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector
from admin.utils import login_required

add_airport_bp = Blueprint('add_airport_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@add_airport_bp.route('/admin/add_airport', methods=['GET', 'POST'])
@login_required
def add_airport():
    if request.method == 'POST':
        try:
            airport_name = request.form.get('aname').upper()

            connection = get_db_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT airport_name FROM airports WHERE airport_name = %s", (airport_name,))
                if cursor.fetchone():
                    error_message = 'The Airport already exists.'
                    flash(error_message)
                    return redirect(url_for('admin.add_airport_bp.add_airport'))
                else:
                    insert_query = "INSERT INTO airports (airport_name) VALUES (%s)"
                    cursor.execute(insert_query, (airport_name,))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return render_template('admin/airport_success.html', airport_name=airport_name)
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
            return redirect(url_for('admin.add_airport_bp.add_airport'))

    return render_template('admin/add_airport.html')
