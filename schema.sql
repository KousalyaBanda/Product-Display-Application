CREATE DATABASE IF NOT EXISTS product_store;
USE product_store;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT
);

INSERT INTO products (name, price, description) VALUES
('Laptop', 70000.00, 'A reliable laptop for work, study, and everyday tasks.'),
('iPhone', 87000.00, 'A premium smartphone with a bright display and powerful camera.'),
('Headphones', 2499.00, 'Comfortable headphones for music, calls, and focus.'),
('Smart Watch', 5999.00, 'Track activity and stay connected throughout the day.');
