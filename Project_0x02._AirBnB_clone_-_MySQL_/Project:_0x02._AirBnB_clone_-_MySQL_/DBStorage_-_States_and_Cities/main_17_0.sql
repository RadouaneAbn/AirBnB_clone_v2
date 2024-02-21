-- Doc
USE hbnb_dev_db;
INSERT INTO states (id, name, created_at, updated_at) VALUES ("my_id_c", "California", CURDATE(), CURDATE());
INSERT INTO states (id, name, created_at, updated_at) VALUES ("my_id_a", "Arizona", CURDATE(), CURDATE());

INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_0", "my_id_c", "San Francisco", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_1", "my_id_c", "San Jose", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_2", "my_id_c", "Los Angeles", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_3", "my_id_c", "Fremont", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_4", "my_id_c", "Palo Alto", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_5", "my_id_c", "Oakland", CURDATE(), CURDATE());

INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_a_0", "my_id_a", "Page", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_a_1", "my_id_a", "Phoenix", CURDATE(), CURDATE());
