
# admin/routes.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import mysql.connector
from airports import fetch_airports
from admin.utils import login_required

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
@login_required
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

@admin_dashboard_bp.route('/add_new_plane', methods=['GET','POST'])
@login_required
def add_new_plane():
    # Logic or rendering for adding a new plane page
    airports = fetch_airports()
    if airports is None:
        flash("An error occurred while fetching airports.")
    elif not airports:
        flash("No airports found.")
        
    return render_template('admin/new_flight.html', airports=airports)

@admin_dashboard_bp.route('/add_airport', methods=['GET','POST'])
@login_required
def add_airport():
    # Logic or rendering for adding a new airport page
    return render_template('admin/add_airport.html')

@admin_dashboard_bp.route('/add_fare', methods=['GET','POST'])
@login_required
def add_fare():
    # Logic or rendering for adding fare page
    airports = fetch_airports()
    if airports is None:
        flash("An error occurred while fetching airports.")
    elif not airports:
        flash("No airports found.")

    return render_template('admin/add_fare.html', airports=airports)

@admin_dashboard_bp.route('/ticket_admin', methods=['GET', 'POST'])
@login_required
def ticket_admin():
    airports = fetch_airports()
    if airports is None: #to automatic airports retriving
        flash("An error occurred while fetching airports.")
    elif not airports:
        flash("No airports found.")
    return render_template('admin/ticket_admin.html', airports=airports)


@admin_dashboard_bp.route('/ticket_admin1', methods=['GET', 'POST'])
@login_required
def ticket_admin1():
    if request.method == 'POST':
        session['step1_data'] = request.form.to_dict()
        return redirect(url_for('admin_dashboard_bp.ticket_admin2'))
    return render_template('admin/ticket_admin1.html')

@admin_dashboard_bp.route('/ticket_admin2', methods=['GET', 'POST'])
@login_required
def ticket_admin2():
    if request.method == 'POST':
        session['step2_data'] = request.form.to_dict()
        return redirect(url_for('admin_dashboard_bp.ticket_admin21'))
    return render_template('admin/ticket_admin2.html')

@admin_dashboard_bp.route('/ticket_admin21', methods=['GET', 'POST'])
@login_required
def ticket_admin21():
    step1_data = session.get('step1_data', {})
    step2_data = session.get('step2_data', {})
    # Combine data from both steps
    combined_data = {**step1_data, **step2_data}
    return render_template('admin/ticket_admin2.html', combined_data=combined_data)

@admin_dashboard_bp.route('/ticket_admin3', methods=['GET', 'POST'])
@login_required
def ticket_admin3():
    if request.method == 'POST':
        # Save step 3 data in session
        session['step4_data'] = request.form.to_dict()#for calculated fare with adult and calculated discounts class fares
        pnames = request.form.getlist('pname[]')
        session['step3_data'] = {
    'pnames': pnames,
    'pnames_upper': [name.upper() for name in pnames],
    'page1': request.form.getlist('page1[]'),
    'pgen1': request.form.getlist('pgen1[]'),
    'ad': request.form.get('ad'),
    'ch': request.form.get('ch'),
    'adm': request.form.get('adm'),
}
        
        return redirect(url_for('admin_dashboard_bp.ticket_admin31'))
    
    return render_template('admin/ticket_admin3.html')

@admin_dashboard_bp.route('/ticket_admin31', methods=['GET', 'POST'])
@login_required
def ticket_admin31():
    # Retrieve all step data from session
    step1_data = session.get('step1_data', {})
    step2_data = session.get('step2_data', {})
    step3_data = session.get('step3_data', {})
    step4_data = session.get('step4_data', {})#for calculated fare with adult and calculated discounts class fares

    # Combine all step data
    combined_data1 = {**step1_data, **step2_data, **step3_data, **step4_data}

    return render_template('admin/ticket_admin3.html', combined_data1=combined_data1)


@admin_dashboard_bp.route('/ticket_success', methods=['GET','POST'])
def ticket_admin_su():
    # Logic or rendering for ticket in index page
    return render_template('admin/ticket_admin_su.html')


# Uncomment and implement as needed
#@admin_dashboard_bp.route('/admin_pnr', methods=['GET'])
#def admin_pnr():
#    # Logic or rendering for admin PNR management page
#    return render_template('admin/admin_pnr.html')

# Additional routes for other admin functionalities
