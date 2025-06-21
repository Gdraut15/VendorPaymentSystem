from flask import Blueprint, request, jsonify
from config.db_config import create_connection

vendor_routes = Blueprint('vendor_routes', __name__)

@vendor_routes.route('/add_vendor', methods=['POST'])
def add_vendor():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    gst_number = data.get('gst_number')

    if not name:
        return jsonify({'error': 'Vendor name is required'}), 400

    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO vendors (name, email, phone, gst_number) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, phone, gst_number))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Vendor added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
