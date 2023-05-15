CREATE DATABASE photo_db;
\c photo_db

CREATE TABLE photos(
    id SERIAL PRIMARY KEY,
    name TEXT,
    image_url TEXT
);

INSERT INTO photos(name, image_url)
VALUES
('ABANDONED FLOWER','https://i.pinimg.com/474x/f5/b7/93/f5b7936bfcb4230b26bbf57f99ad4aa9.jpg');

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
);

ALTER TABLE users ADD COLUMN password_digest TEXT;

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    user_comment TEXT,
    photo_id INT,
    user_id INT
);

