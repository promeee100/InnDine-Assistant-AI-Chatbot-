CREATE DATABASE hotel_restaurant;

USE hotel_restaurant;

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_type VARCHAR(50),
    price_per_night FLOAT,
    is_available BOOLEAN DEFAULT TRUE
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    room_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    food_item VARCHAR(100),
    quantity INT,
    order_date DATE
);

INSERT INTO rooms (room_type, price_per_night, is_available) VALUES
('Single', 50, TRUE),
('Double', 80, TRUE),
('Suite', 150, TRUE);
