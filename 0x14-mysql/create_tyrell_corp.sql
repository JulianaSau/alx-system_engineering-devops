-- create_tyrell_corp.sql

-- Create the tyrell_corp database if it doesn't exist
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Switch to the tyrell_corp database
USE tyrell_corp;

-- Create the nexus6 table if it doesn't exist
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    model VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert an entry into the nexus6 table
INSERT INTO nexus6 (name, model) VALUES ('Nexus 6', 'Replicant');

-- Grant SELECT permissions on the nexus6 table to the holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
