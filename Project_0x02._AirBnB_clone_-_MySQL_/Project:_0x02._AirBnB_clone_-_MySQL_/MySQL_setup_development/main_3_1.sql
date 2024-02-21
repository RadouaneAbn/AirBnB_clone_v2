-- Create table + Insert + Select
USE hbnb_dev_db;
CREATE TABLE IF NOT EXISTS test_table ( 
    id INT, 
    name VARCHAR(256)
);
INSERT INTO test_table (id, name) VALUES (89, "Holberton School");
SELECT id, name FROM test_table ORDER BY id ASC;
