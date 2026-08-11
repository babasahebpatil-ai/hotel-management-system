from flask import Flask, render_template, request, redirect, url_for, session, flash
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'hotel_secret_key'


# =========================================================
# POSTGRESQL CONNECTION
# =========================================================

db = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="root",
    database="hotel_management"
)

cursor = db.cursor(cursor_factory=RealDictCursor)


# =========================================================
# AUTH SYSTEM
# =========================================================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']

        password = generate_password_hash(
            request.form['password']
        )

        try:

            cursor.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
                """,
                (name, email, password)
            )

            db.commit()

            flash(
                'Registration successful! Please login.',
                'success'
            )

            return redirect(url_for('login'))

        except IntegrityError:

            db.rollback()

            flash(
                'Email already registered. Please log in instead.',
                'danger'
            )

            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )

        user = cursor.fetchone()

        if user and check_password_hash(
            user['password'],
            password
        ):

            session['user_id'] = user['id']
            session['user_name'] = user['name']

            flash(
                f"Welcome back, {user['name']}!",
                'info'
            )

            return redirect(url_for('home'))

        else:

            flash(
                'Invalid credentials. Try again.',
                'danger'
            )

    return render_template('login.html')


@app.route('/logout')
def logout():

    session.clear()

    flash(
        'Logged out successfully.',
        'info'
    )

    return redirect(url_for('login'))


# =========================================================
# LOGIN PROTECTION
# =========================================================

@app.before_request
def require_login():

    allowed_routes = [
        'login',
        'register',
        'static'
    ]

    if (
        request.endpoint not in allowed_routes
        and 'user_id' not in session
    ):
        return redirect(url_for('login'))


# =========================================================
# DASHBOARD
# =========================================================

@app.route('/')
def home():

    user_name = session.get(
        'user_name',
        'Guest'
    )

    return render_template(
        'index.html',
        user_name=user_name
    )


# =========================================================
# BOOKINGS
# =========================================================

@app.route('/bookings')
def bookings():

    cursor.execute(
        "SELECT * FROM bookings ORDER BY id DESC"
    )

    data = cursor.fetchall()

    return render_template(
        'booking.html',
        bookings=data
    )


@app.route('/add_booking', methods=['POST'])
def add_booking():

    contact = request.form['contact']
    checkin = request.form['checkin']
    checkout = request.form['checkout']
    room_type = request.form['room_type']
    room_no = request.form['room_no']
    meal = request.form['meal']
    days = request.form['days']
    subtotal = request.form['subtotal']
    tax = request.form['tax']
    total = request.form['total']

    cursor.execute(
        """
        INSERT INTO bookings
        (
            customer_contact,
            checkin_date,
            checkout_date,
            room_type,
            room_no,
            meal,
            no_of_days,
            subtotal,
            tax,
            total
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            contact,
            checkin,
            checkout,
            room_type,
            room_no,
            meal,
            days,
            subtotal,
            tax,
            total
        )
    )

    db.commit()

    return redirect(
        url_for('bookings')
    )


@app.route('/update_booking', methods=['POST'])
def update_booking():

    booking_id = request.form['id']

    contact = request.form['contact']
    checkin = request.form['checkin']
    checkout = request.form['checkout']
    room_type = request.form['room_type']
    room_no = request.form['room_no']
    meal = request.form['meal']
    days = request.form['days']
    subtotal = request.form['subtotal']
    tax = request.form['tax']
    total = request.form['total']

    cursor.execute(
        """
        UPDATE bookings
        SET
            customer_contact = %s,
            checkin_date = %s,
            checkout_date = %s,
            room_type = %s,
            room_no = %s,
            meal = %s,
            no_of_days = %s,
            subtotal = %s,
            tax = %s,
            total = %s
        WHERE id = %s
        """,
        (
            contact,
            checkin,
            checkout,
            room_type,
            room_no,
            meal,
            days,
            subtotal,
            tax,
            total,
            booking_id
        )
    )

    db.commit()

    return redirect(
        url_for('bookings')
    )


@app.route('/delete_booking/<int:id>')
def delete_booking(id):

    cursor.execute(
        "DELETE FROM bookings WHERE id = %s",
        (id,)
    )

    db.commit()

    return redirect(
        url_for('bookings')
    )


# =========================================================
# CUSTOMERS
# =========================================================

@app.route('/customers')
def customers():

    cursor.execute(
        "SELECT * FROM customers ORDER BY id DESC"
    )

    customers_data = cursor.fetchall()

    return render_template(
        'customer.html',
        customers=customers_data
    )


@app.route('/add_customer', methods=['POST'])
def add_customer():

    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    nationality = request.form['nationality']
    address = request.form['address']
    contact = request.form['contact']

    cursor.execute(
        """
        INSERT INTO customers
        (
            name,
            gender,
            email,
            nationality,
            address,
            contact
        )
        VALUES
        (%s, %s, %s, %s, %s, %s)
        """,
        (
            name,
            gender,
            email,
            nationality,
            address,
            contact
        )
    )

    db.commit()

    return redirect(
        url_for('customers')
    )


# =========================================================
# REPORTS
# =========================================================

@app.route('/reports')
def reports():

    cursor.execute(
        """
        SELECT
            COUNT(*) AS total_bookings,
            COALESCE(SUM(total), 0) AS total_revenue
        FROM bookings
        """
    )

    report = cursor.fetchone()

    cursor.execute(
        """
        SELECT
            room_type,
            COALESCE(SUM(total), 0) AS revenue
        FROM bookings
        GROUP BY room_type
        ORDER BY room_type
        """
    )

    data = cursor.fetchall()

    room_labels = [
        row['room_type']
        for row in data
    ]

    room_data = [
        float(row['revenue'])
        if row['revenue'] is not None
        else 0
        for row in data
    ]

    return render_template(
        'report.html',
        report=report,
        room_labels=room_labels,
        room_data=room_data
    )


# =========================================================
# DELETE CUSTOMER
# =========================================================

@app.route('/delete_customer/<int:id>')
def delete_customer(id):

    cursor.execute(
        "DELETE FROM customers WHERE id = %s",
        (id,)
    )

    db.commit()

    return redirect(
        url_for('customers')
    )


# =========================================================
# UPDATE CUSTOMER
# =========================================================

@app.route('/update_customer/<int:id>', methods=['GET', 'POST'])
def update_customer(id):

    if request.method == 'POST':

        name = request.form['name']
        gender = request.form['gender']
        email = request.form['email']
        nationality = request.form['nationality']
        address = request.form['address']
        contact = request.form['contact']

        cursor.execute(
            """
            UPDATE customers
            SET
                name = %s,
                gender = %s,
                email = %s,
                nationality = %s,
                address = %s,
                contact = %s
            WHERE id = %s
            """,
            (
                name,
                gender,
                email,
                nationality,
                address,
                contact,
                id
            )
        )

        db.commit()

        return redirect(
            url_for('customers')
        )

    else:

        cursor.execute(
            "SELECT * FROM customers WHERE id = %s",
            (id,)
        )

        customer = cursor.fetchone()

        return render_template(
            'update_customer.html',
            customer=customer
        )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == '__main__':
    app.run(debug=True)