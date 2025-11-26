
CREATE DATABASE IF NOT EXISTS hotel_chatbot;
USE hotel_chatbot;

CREATE TABLE IF NOT EXISTS rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_type VARCHAR(50),
    price_per_night DECIMAL(10,2),
    is_available BOOLEAN DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    room_id INT,
    check_in DATE,
    check_out DATE,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);


CREATE TABLE IF NOT EXISTS food_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    food_item VARCHAR(100),
    quantity INT,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO rooms (room_type, price_per_night, is_available) VALUES
('Single Deluxe', 80.00, TRUE),
('Double Deluxe', 120.00, TRUE),
('Suite', 200.00, TRUE);
