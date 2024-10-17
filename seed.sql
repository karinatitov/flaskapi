-- Create customer table if it doesn't exist
CREATE TABLE IF NOT EXISTS customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    zip VARCHAR(20)
);

-- Insert seed data
INSERT INTO customer (first_name, last_name, email, address, city, state, zip)
VALUES
('Jane', 'Doe', 'jane.doe@example.com', '456 Oak St', 'San Antonio', 'TX', '78205'),
('Alice', 'Smith', 'alice.smith@example.com', '789 Pine St', 'Austin', 'TX', '73301'),
('Bob', 'Johnson', 'bob.johnson@example.com', '123 Elm St', 'Dallas', 'TX', '75201');