
CREATE TABLE emotions (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    emotion VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
