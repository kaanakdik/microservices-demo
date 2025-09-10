CREATE DATABASE IF NOT EXISTS user_service_db;

USE user_service_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO users (name, email) VALUES
('Kaan', 'kaan@example.com'),
('Ahmet', 'ahmet@example.com'),
('Ayşe', 'ayse@example.com'),
('Harun', 'harun@example.com'),
('Necla', 'necla@example.com');
