# user/routes.py for html programs

from flask import Blueprint, render_template, flash
from airports import fetch_airports
import mysql.connector
from user.utils import login_required

user_dashboard_bp = Blueprint('user_dashboard_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

# Function to get database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

@user_dashboard_bp.route('/dashboard', methods=['GET','POST'])
@login_required
def user_dashboard():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Example query to fetch user data
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, ('user',))
        user_data = cursor.fetchone()

        # Close cursor and connection
        cursor.close()
        conn.close()

        return render_template('user/welcome_user.html', user=user_data)

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        # Handle database connection error gracefully, e.g., show error page
        return render_template('error.html', error_message='Database connection error')
    
@user_dashboard_bp.route('/ticket_user', methods=['GET', 'POST'])
@login_required
def ticket_user():
    airports = fetch_airports()
    if airports is None: #to automatic airports retriving
        flash("An error occurred while fetching airports.")
    elif not airports:
        flash("No airports found.")
    return render_template('user/ticket_user.html', airports=airports)

@user_dashboard_bp.route('/tck_user', methods=['GET','POST'])
@login_required
def ticket_user1():
    # Logic or rendering for ticket in index page
    return render_template('user/ticket_user1.html')

@user_dashboard_bp.route('/tck_user2', methods=['GET','POST'])
@login_required
def ticket_user2():
    # Logic or rendering for ticket in index page
    return render_template('user/ticket_user2.html')


#@user_dashboard_bp.route('/user_pnr', methods=['GET'])
#def user_pnr():
    # Logic or rendering for user PNR management page
   # return render_template('user/user_pnr.html')

# Additional routes for other user functionalities
