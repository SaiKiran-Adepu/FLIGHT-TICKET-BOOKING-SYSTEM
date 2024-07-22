from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector
from admin.utils import login_required

add_fare_bp = Blueprint('add_fare_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@add_fare_bp.route('/admin/add_fare', methods=['GET', 'POST'])
@login_required
def add_fare():
    if request.method == 'POST':
         try:
            airport = request.form['airport']
            fare = request.form['fare']
            kmf = request.form['km']
            aadm = request.form['adm']
            airport1, airport2 = airport.split(',')

            connection = get_db_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT airport FROM airplane_fare WHERE FIND_IN_SET(%s, airport) AND FIND_IN_SET(%s, airport)", (airport1, airport2,))
                if cursor.fetchone():
                    error_message = 'The Airport with the specified fare and distance already exists.'
                    flash(error_message)
                    return redirect(url_for('admin.add_fare_bp.add_fare'))
                else:
                    insert_query = "INSERT INTO airplane_fare (airport, fare, km, aad) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (airport, fare, kmf, aadm))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return render_template('admin/fare_success.html', airport=airport, fare=fare, kmf=kmf, aadm=aadm)
         except Exception as e:
            flash(f"An error occurred: {str(e)}")
            return redirect(url_for('admin.add_fare_bp.add_fare'))

    return render_template('admin/add_fare.html')
