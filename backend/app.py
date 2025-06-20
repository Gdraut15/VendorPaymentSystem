from flask import render_template
from flask_mail import Mail, Message
from flask import jsonify

# inside your route
msg = Message(
    subject='Payment Notification',
    sender='your_email@example.com',
    recipients=[vendor_email],
    html=render_template('email_template.html',
                         vendor_name=vendor_name,
                         invoice=invoice,
                         amount=amount,
                         gst_amount=gst_amount,
                         tds_amount=tds_amount,
                         net_amount=net_amount,
                         date=payment_date)
)
mail.send(msg)

@app.route('/api/payments')
def get_payments():
    # Replace this with DB query or actual data
    dummy_data = [
        {
            "invoice": "INV001",
            "vendor": "Vendor A",
            "gross": 10000,
            "gst": 1800,
            "tds": 1000,
            "net": 7200,
            "date": "2025-06-17"
        },
        {
            "invoice": "INV002",
            "vendor": "Vendor B",
            "gross": 5000,
            "gst": 900,
            "tds": 500,
            "net": 3600,
            "date": "2025-06-15"
        }
    ]
    return jsonify(dummy_data)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# TODO: Add SMS notification here using vendor's phone number
# Example message:
# "[NTPS] Hello {vendor_name}, your payment of ₹{net_amount}..."


# TODO: Integrate SMS sending here
