from flask import Blueprint, request, jsonify
from config.db_config import create_connection
from datetime import date

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('/add_payment', methods=['POST'])
def add_payment():
    data = request.get_json()
    vendor_id = data.get('vendor_id')
    amount = data.get('amount')

    if not vendor_id or not amount:
        return jsonify({'error': 'vendor_id and amount are required'}), 400

    try:
        amount = float(amount)
        gst = round(0.18 * amount, 2)  # 18% GST
        tds = round(0.10 * amount, 2)  # 10% TDS
        payment_date = date.today()

        conn = create_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO payments (vendor_id, amount, gst, tds, payment_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (vendor_id, amount, gst, tds, payment_date))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            'message': 'Payment added successfully',
            'data': {
                'vendor_id': vendor_id,
                'amount': amount,
                'gst': gst,
                'tds': tds,
                'payment_date': str(payment_date)
            }
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
