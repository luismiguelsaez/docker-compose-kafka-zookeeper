
CREATE TABLE IF NOT EXISTS objects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

INSERT INTO objects (name) VALUES ("obj1");
INSERT INTO objects (name) VALUES ("obj2");
INSERT INTO objects (name) VALUES ("obj3");
INSERT INTO objects (name) VALUES ("obj4");