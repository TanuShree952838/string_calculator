CREATE TABLE IF NOT EXISTS calculations (
    id SERIAL PRIMARY KEY,
    input_text TEXT NOT NULL,
    result INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
