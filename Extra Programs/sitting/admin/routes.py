from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import mysql.connector
from admin.airports import fetch_airports

admin_dashboard_bp = Blueprint('admin_dashboard_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'your_adminname',
    'password': 'your_password',
    'database': 'your_database'
}

# Function to get database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

@admin_dashboard_bp.route('/dashboard', methods=['GET','POST'])

def admin_dashboard():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Example query to fetch admin data
        query = "SELECT * FROM admins WHERE adminname = %s"
        cursor.execute(query, ('Admin',))
        admin_data = cursor.fetchone()

        # Close cursor and connection
        cursor.close()
        conn.close()

        return render_template('admin/welcome_admin.html', admin=admin_data)
    
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        # Handle database connection error gracefully, e.g., show error page
        return render_template('error.html', error_message='Database connection error')
    

    #TICKET BOOKING
@admin_dashboard_bp.route('/ticket_admin', methods=['GET', 'POST'])
def ticket_admin():
    airports = fetch_airports()
    if airports is None: #to automatic airports retriving
        flash("An error occurred while fetching airports.")
    elif not airports:
        flash("No airports found.")
    return render_template('admin/ticket_admin.html', airports=airports)

@admin_dashboard_bp.route('/ticket_admin1', methods=['GET', 'POST'])
def ticket_admin1():
    return render_template('admin/ticket_admin1.html')
