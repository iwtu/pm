CREATE DATABASE pmdb;

\c pmdb;

CREATE TABLE user_values (
    email text PRIMARY KEY,
    value text NOT NULL    
);