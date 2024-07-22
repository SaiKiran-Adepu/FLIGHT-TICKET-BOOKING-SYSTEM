from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector
from admin.utils import login_required

ticket_admindb_bp = Blueprint('ticket_admindb_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def generate_seat_numbers(num_passengers, class_type):
    seat_prefix = {
        'FIRST CLASS': '1A 1B 1C 1D 2A 2B 2C 2D 3A 3B 3C 3D'.split(),
        'BUSINESS CLASS': '4A 4B 4C 4D 5A 5B 5C 5D 6A 6B 6C 6D'.split(),
        'PREMIUM ECONOMY': '7A 7B 7C 7D 8A 8B 8C 8D 9A 9B 9C 9D'.split(),
        'ECONOMY': '10A 10B 10C 10D 11A 11B 11C 11D 12A 12B 12C 12D'.split()
    }
    seats = seat_prefix.get(class_type, [])
    if not seats:
        raise ValueError(f"No seats available for flight class: {class_type}")
    return [seats[i % len(seats)] for i in range(num_passengers)]

@ticket_admindb_bp.route('/ticket_admin_su', methods=['GET', 'POST'])
@login_required
def ticket_admindb():
    # Retrieve all step data from session
    step1_data = session.get('step1_data', {})
    step2_data = session.get('step2_data', {})
    step3_data = session.get('step3_data', {})
    step4_data = session.get('step4_data', {})

    # Combine all step data
    combined_data1 = {**step1_data, **step2_data, **step3_data, **step4_data}

    if request.method == 'POST':
        connection = None
        cursor = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            dob = request.form['dob']# called from last form
            
            # Start transaction
            connection.start_transaction()

            # Insert into airline_reservation table
            insert_reservation_query = """
                INSERT INTO airline_reservation (
                    flight_number, flight_name, origin, dest, flight_class, quota_type,
                    adult, child, base_fare, class_fare, quota_fare, quota_discount,
                    trip_mode, trip_discount, fare, km, booked_on, jd, rd,booked_by
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Execute the reservation insertion
            cursor.execute(insert_reservation_query, (
                combined_data1.get('flight_number', ''),
                combined_data1.get('flight_name', ''),
                combined_data1.get('origin', ''),
                combined_data1.get('dest', ''),
                combined_data1.get('class_type', ''),
                combined_data1.get('ticket_type', ''),
                combined_data1.get('ad', 0),
                combined_data1.get('ch', 0),
                combined_data1.get('base_fare', 0),
                combined_data1.get('class_charge1', 0),
                combined_data1.get('quota_fare', 0),
                combined_data1.get('quota_discount1', 0),
                combined_data1.get('trip_mode', ''),
                combined_data1.get('trip_discount1', 0),
                combined_data1.get('total_fare1', 0),
                combined_data1.get('km', 0),
                dob,# because called from last form without from routes at the perfect time of booking
                #combined_data1.get('dob', ''),
                combined_data1.get('jdt', ''),
                combined_data1.get('rdt', ''),
                combined_data1.get('adm', '')
            ))
            
            reservation_id = cursor.lastrowid

            # Insert into airline_sitting table
            pname_values = combined_data1.get('pnames', [])
            page_values = combined_data1.get('page1', [])
            pgen_values = combined_data1.get('pgen1', [])
            adm=combined_data1.get('adm', '')

            insert_sitting_query = """
                INSERT INTO airline_sitting (PNR, name, age, gender, seat_number, ausr, aadm)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            try:
                seat_numbers = generate_seat_numbers(len(pname_values), combined_data1.get('class_type', ''))
            except ValueError as e:
                flash(str(e))
                connection.rollback()
                return redirect(url_for('admin.ticket_admindb_bp.ticket_admindb'))

            sitting_details = []

            for i in range(len(pname_values)):
                cursor.execute(insert_sitting_query, (
                    reservation_id, pname_values[i], page_values[i], pgen_values[i], seat_numbers[i], None, adm
                ))
                sitting_details.append({
                    'name': pname_values[i],
                    'age': page_values[i],
                    'gender': pgen_values[i],
                    'seat_number': seat_numbers[i]
                })

            # Commit the transaction if both inserts are successful
            connection.commit()
            cursor.close()
            connection.close()

            return render_template('admin/ticket_admin_su.html', orn=combined_data1['origin'], dest=combined_data1['dest'], jdt=combined_data1['jdt'],rdt=combined_data1['rdt'], clt=combined_data1['class_type'], tt=combined_data1['ticket_type'], 
                                   ad=combined_data1['ad'],ch=combined_data1['ch'],bsf=combined_data1['base_fare'],qdt=combined_data1['quota_discount1'],cf=combined_data1['class_charge1'],
                                   trm=combined_data1['trip_mode'],td=combined_data1['trip_discount1'],tf=combined_data1['total_fare1'],km=combined_data1['km'],flight_number=combined_data1['flight_number'], flight_name=combined_data1['flight_name'], sitting_details=sitting_details)
        except Exception as e:
            if connection:
                connection.rollback()
            if cursor:
                cursor.close()
            if connection:
                connection.close()
            flash(f"An error occurred with the airline_reservation: {str(e)}")
            return redirect(url_for('admin.ticket_admindb_bp.ticket_admindb'))

    return render_template('admin/ticket_admin3.html', combined_data1=combined_data1)
