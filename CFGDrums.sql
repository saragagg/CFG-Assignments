CREATE DATABASE CFGDrums;

USE CFGDrums;

CREATE TABLE instructors
(id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
bio VARCHAR(400),
email_address VARCHAR(150) UNIQUE NOT NULL);

CREATE TABLE students
(id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
email_address VARCHAR(150) UNIQUE NOT NULL,
phone_number VARCHAR(15) NOT NULL,
disability_requirements TEXT
);

CREATE TABLE classes 
(id INT AUTO_INCREMENT PRIMARY KEY,
class_name VARCHAR(150) NOT NULL,
schedule DATETIME NOT NULL,
description VARCHAR(350) NOT NULL,
available_spots INT NOT NULL,
instructor_id INT NOT NULL,
FOREIGN KEY (instructor_id) REFERENCES instructors(id));

INSERT INTO instructors
(first_name, last_name, bio, email_address)
VALUES
('Martin', 'Gordon', 'An experienced drummer with over 20 years of performing and teaching experience.', 'martin.gordon@example.com'),
('Adam', 'Smith', 'Specializes in jazz drumming and has been teaching for 15 years.', 'adam.smith@example.com'),
('Megan', 'Johnson', 'A rock drumming expert who has toured with several famous bands.', 'megan.johnson@example.com');

INSERT INTO classes
(class_name, schedule, description, available_spots, instructor_id)
VALUES
('Beginner Drums', '2024-07-05 10:00:00', 'An introductory class for beginner drummers.', 10, 1),
('Intermediate Drums', '2024-07-06 14:00:00', 'For those with some drumming experience looking to improve.', 8, 2),
('Advanced Drums', '2024-07-07 16:00:00', 'A class for advanced drummers to refine their skills.', 5, 3);

INSERT INTO students
(first_name, last_name, email_address, phone_number, disability_requirements)
VALUES
('Alice', 'Brown', 'alice.brown@example.com', '07123456789', NULL),
('Charlie', 'Davis', 'charlie.davis@example.com', '07987654321', NULL),
('Eve', 'Foster', 'eve.foster@example.com', '07112233445', 'Requires wheelchair access.'),
('Grace', 'Hall', 'grace.hall@example.com', '07567890123', NULL),
('Henry', 'King', 'henry.king@example.com', '07654321890', 'Needs assistance with hearing impairment.');


--DROP DATABASE IF EXISTS CFGDrums;
