# index users/or guest users to site routes.py
from flask import Blueprint, render_template, flash
from airports import fetch_airports

guest_dashboard_bp = Blueprint('guest_dashboard_bp', __name__)

@guest_dashboard_bp.route('/airlin_admins', methods=['GET','POST'])
def airline_admins():
    # Logic or rendering for ticket in index page
    return render_template('airline_admins.html')

@guest_dashboard_bp.route('/ticket_index', methods=['GET', 'POST'])
def ticket_index():
    airports = fetch_airports()
    if airports is None: #to automatic airports retriving
        flash("An error occurred while fetching airports.")
    elif not airports:
        flash("No airports found.")
    return render_template('guest/ticket_index.html', airports=airports)

@guest_dashboard_bp.route('/tck_index', methods=['GET','POST'])
def ticket_index_su():
    # Logic or rendering for ticket in index page
    return render_template('guest/ticket_index_su.html')

@guest_dashboard_bp.route('/pnr_index', methods=['GET','POST'])
def pnr_index():
    # Logic or rendering for ticket in index page
    return render_template('guest/pnr_index.html')

@guest_dashboard_bp.route('/plane_schedule', methods=['GET','POST'])
def plane_schedule():
    # Logic or rendering for ticket in index page
    return render_template('guest/plane_schedule.html')

@guest_dashboard_bp.route('/user_register', methods=['GET','POST'])
def user_register():
    # Logic or rendering for ticket in index page
    return render_template('guest/user_register.html')

@guest_dashboard_bp.route('/register_success', methods=['GET','POST'])
def register_success():
    # Logic or rendering for ticket in index page
    return render_template('guest/register_success.html')

@guest_dashboard_bp.route('/instructions', methods=['GET','POST'])
def instructions():
    # Logic or rendering for ticket in index page
    return render_template('guest/instructions.html')

@guest_dashboard_bp.route('/newsevents_index', methods=['GET','POST'])
def newsevents_index():
    # Logic or rendering for ticket in index page
    return render_template('guest/newsevents_index.html')

@guest_dashboard_bp.route('/feedback_index', methods=['GET','POST'])
def feedback_index():
    # Logic or rendering for ticket in index page
    return render_template('guest/feedback_index.html')

@guest_dashboard_bp.route('/feedback_index_su', methods=['GET','POST'])
def feedback_index_su():
    # Logic or rendering for ticket in index page
    return render_template('guest/feedback_index_su.html')
# Uncomment and complete this route if needed
# @guest_dashboard_bp.route('/guest_pnr', methods=['GET'])
# def guest_pnr():
#     # Logic or rendering for guest PNR management page
#     return render_template('guest/guest_pnr.html')

# Additional routes for other guest functionalities
