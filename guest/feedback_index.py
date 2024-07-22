from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector

feedback_index_bp = Blueprint('feedback_index_bp', __name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@feedback_index_bp.route('/guest/feedback_index', methods=['GET', 'POST'])
def feedback_index():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form['name']
            feed = request.form['feed']  # Ensure unique usernames or handle duplicates
            dofdb = request.form['dofdb']

            # Database operations
            con = get_db_connection()
            cursor = con.cursor()

            # Insert user details
            insert_query = """
                INSERT INTO airline_ufeedback (name, feedback, dateofeed)
                VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (name, feed, dofdb))
            con.commit()

            cursor.close()
            con.close()

            return render_template('guest/feedback_index_su.html', user_details={'name': name, 'feedback': feed, 'dateofeed': dofdb})

        except Exception as ex:
            print(ex)
            error_message = 'An error occurred during feedback. Please try again.'
            flash(error_message)
            return redirect(url_for('feedback_index_bp.feedback_index'))
    
    return render_template('guest/feedback_index.html')
