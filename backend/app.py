from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from routes import register_routes

app = Flask(__name__)
CORS(app)

# Mail dummy config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'demo.project.email@gmail.com'
app.config['MAIL_PASSWORD'] = 'demo-app-password'

# Init mail
mail = Mail(app)

# Register routes
register_routes(app)

# Expose mail globally
import builtins
builtins.mail = mail

if __name__ == '__main__':
    print("🚀 Flask starting...")
    app.run(debug=True)
