from .auth import auth_routes
from .vendor import vendor_routes
from .payment import payment_routes

from .auth import auth_routes
from .vendor import vendor_routes
from .payment import payment_routes

def register_routes(app):
    print("✅ Registering routes...")
    app.register_blueprint(auth_routes)
    app.register_blueprint(vendor_routes)
    app.register_blueprint(payment_routes)

