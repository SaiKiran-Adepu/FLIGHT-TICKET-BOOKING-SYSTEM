from flask import Blueprint, render_template, request, jsonify
import mysql.connector

# Define the blueprint
seat_avl_bp = Blueprint('seat_avl_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    """Establish and return a database connection."""
    return mysql.connector.connect(**db_config)
@seat_avl_bp.route('/admin/seat_avl', methods=['GET', 'POST'])
def seat_avl():
    if request.method == 'GET':
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            
            cursor.execute("SELECT flight_Number, flight_Name, jd FROM airline_sitting GROUP BY flight_Number, flight_Name, jd")
            flights = cursor.fetchall()
        except Exception as e:
            flights = []
            print(f"Error fetching flights: {e}")
        finally:
            cursor.close()
            connection.close()

        return render_template('admin/seat_avl.html', flights=flights)
    
    if request.method == 'POST':
        data = request.get_json()
        flight_number = data.get('flight_number')
        flight_name = data.get('flight_name')
        flight_class = data.get('flight_class')
        journey_date = data.get('date')

        seat_layout = {
            'FIRST CLASS': 12,
            'BUSINESS CLASS': 8,
            'PREMIUM ECONOMY': 8,
            'ECONOMY': 12
        }

        result = {}
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            booked_seats_query = """
                SELECT COUNT(*) FROM airline_sitting
                WHERE flight_Number=%s AND flight_Name=%s AND flight_class=%s AND jd=%s
            """
            cursor.execute(booked_seats_query, (flight_number, flight_name, flight_class, journey_date))
            booked_seats = cursor.fetchone()[0]

            available_seats = seat_layout.get(flight_class, 0) - booked_seats
            result[flight_class] = available_seats

        except Exception as e:
            return jsonify({"error": str(e)}), 500

        finally:
            cursor.close()
            connection.close()

        return jsonify(result)