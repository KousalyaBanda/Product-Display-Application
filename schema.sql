CREATE DATABASE IF NOT EXISTS product_store;
USE product_store;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT
);

INSERT INTO products (name, price, description)
SELECT 'Laptop', 70000.00, 'A laptop for work and study.'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Laptop');

INSERT INTO products (name, price, description)
SELECT 'Headphones', 2499.00, 'Headphones for music and calls.'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Headphones');

INSERT INTO products (name, price, description)
SELECT 'Smart Watch', 5999.00, 'A watch for activity tracking.'
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Smart Watch');
