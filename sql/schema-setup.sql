
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(12) NOT NULL,
    content VARCHAR(120) NOT NULL
);

INSERT INTO messages (user,content) VALUES ("john","Good morning all");
INSERT INTO messages (user,content) VALUES ("sarah","Hello from Canada");
INSERT INTO messages (user,content) VALUES ("paul","I'm experiencing connection issues");
INSERT INTO messages (user,content) VALUES ("alice","Setting up my laptop");