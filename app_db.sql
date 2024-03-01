CREATE TABLE Stock (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Item (
    id SERIAL PRIMARY KEY,
    stock_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES Stock(id)
);

CREATE TABLE Admin (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Transaction (
    id SERIAL PRIMARY KEY,
    admin_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES Admin(id),
    FOREIGN KEY (item_id) REFERENCES Item(id)
);
