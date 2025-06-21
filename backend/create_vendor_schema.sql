-- Create the database with a new unique name
DROP DATABASE IF EXISTS vendor_payment_system_db;
CREATE DATABASE vendor_payment_system_db;
USE vendor_payment_system_db;

-- USERS Table
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'user') DEFAULT 'user'
);

-- VENDORS Table
CREATE TABLE vendors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    gst_number VARCHAR(20)
);

-- PAYMENTS Table
CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_id INT,
    amount DECIMAL(10,2),
    gst DECIMAL(10,2),
    tds DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE CASCADE
);
