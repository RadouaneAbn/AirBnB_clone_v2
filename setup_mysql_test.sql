-- script that prepares a MySQL for the project
-- create database hbnb_test_db and user hbnb_test in localhost with pwd hbnb_test_pwd
-- Grant all  priviliges on hbnb_test and selecton on performace_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* To hbnb_test@localhost;
FLUSH PRIVILEGES;
