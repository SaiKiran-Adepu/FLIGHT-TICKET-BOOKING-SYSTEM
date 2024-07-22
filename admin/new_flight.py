from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector
from admin.utils import login_required

new_flight_bp = Blueprint('new_flight_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@new_flight_bp.route('/admin/add_new_plane', methods=['GET', 'POST'])
@login_required
def add_new_plane():
    if request.method == 'POST':
        try:
            flight_number = request.form['flight_number'].upper()
            flight_name = request.form['flight_name'].upper()
            selected_airports = request.form['selected_airports'].upper()
            base_fare = request.form['base_fare']
            first_class = request.form.get('first_class', '').upper()
            business_class = request.form.get('business_class', '').upper()
            premium_economy = request.form.get('premium_economy', '').upper()
            economy = request.form.get('economy', '').upper()

            gen=request.form.get('general', '').upper()
            df=request.form.get('defence', '').upper()
            ge=request.form.get('govt_employee', '').upper()
            sc=request.form.get('senior_citizen', '').upper()
            stn=request.form.get('student', '').upper()




            fadon = request.form['doa']
            fadm = request.form['adm'].upper()

            plane_class = first_class + business_class + premium_economy + economy

            plane_quota = gen + df + ge + sc + stn

            connection = get_db_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT flight_number FROM flights WHERE flight_number = %s", (flight_number,))
                if cursor.fetchone():
                    error_message = 'The Flight Number already exists.'
                    flash(error_message)
                    return redirect(url_for('admin.new_flight_bp.add_new_plane', error_message=error_message))
                else:
                    insert_query = """
                    INSERT INTO flights (flight_number, flight_name, airports, base_fare, class, ticket_type, flight_addedon, flight_admin)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, (flight_number, flight_name, selected_airports, base_fare, plane_class, plane_quota, fadon,fadm))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return render_template('admin/success.html', flight_number=flight_number, flight_name=flight_name, airports=selected_airports, base_fare=base_fare, plane_class=plane_class, plane_quota=plane_quota, fadm=fadm, fadon=fadon )
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
            return redirect(url_for('admin.new_flight_bp.add_new_plane'))

    return render_template('admin/new_flight.html')
