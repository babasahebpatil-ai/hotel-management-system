CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    email VARCHAR(100),
    nationality VARCHAR(50),
    address VARCHAR(200),
    contact VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_contact VARCHAR(15),
    checkin_date DATE,
    checkout_date DATE,
    room_type VARCHAR(20),
    room_no VARCHAR(10),
    meal VARCHAR(50),
    no_of_days INT,
    tax FLOAT,
    subtotal FLOAT,
    total FLOAT
);
