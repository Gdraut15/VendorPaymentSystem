import MySQLdb

def create_connection():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        password="Sakshi@2801@",       # replace with your DB password
        database="vendor_payment_system_db"  # use your actual DB name
    )
