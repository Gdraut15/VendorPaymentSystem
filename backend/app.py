# app.py

from flask import Flask
from flask_cors import CORS
from routes import register_routes  # ✅ Import the route registration function

app = Flask(__name__)   # ✅ Create the Flask app
CORS(app)               # ✅ Enable CORS so frontend can connect

register_routes(app)    # ✅ Register all blueprints like auth, vendor, payment

if __name__ == '__main__':
    app.run(debug=True)  # ✅ Start the Flask development server
