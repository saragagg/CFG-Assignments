
CREATE DATABASE CFGCharity;

USE CFGCharity;

CREATE TABLE donors
(donor_id INT AUTO_INCREMENT PRIMARY KEY,
donor_type ENUM('private donor', 'government entity') NOT NULL,
donor_name VARCHAR(100) NOT NULL,
contact_person VARCHAR(100),
email_address VARCHAR(100) UNIQUE NOT NULL,
phone_number VARCHAR(15),
address VARCHAR(250));
# can be private donor or government funded entity which will have a contact person. Name can be either full name for private donor or entity name 

CREATE TABLE beneficiaries
(beneficiary_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(50) NOT NULL,
address VARCHAR(250) NOT NULL,
phone_number VARCHAR(15) NOT NULL,
email_address VARCHAR(100) UNIQUE,
family_size INT
);

CREATE TABLE categories
(category_id INT AUTO_INCREMENT PRIMARY KEY,
category_name VARCHAR(70)
);

CREATE TABLE donations
(donation_id INT AUTO_INCREMENT PRIMARY KEY,
quantity INT NOT NULL CHECK (quantity > 0),
donation_date DATE NOT NULL,
donor_id INT NOT NULL,
FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
);


CREATE TABLE items
(item_id INT AUTO_INCREMENT PRIMARY KEY,
item_name VARCHAR(150) NOT NULL,
category_id INT,
quantity INT NOT NULL CHECK (quantity >= 0),
expiry_date DATE,
donation_id INT,
description TEXT,
FOREIGN KEY (category_id) REFERENCES categories(category_id),
FOREIGN KEY (donation_id) REFERENCES donations(donation_id)
);

CREATE TABLE distributions
(distribution_id INT AUTO_INCREMENT PRIMARY KEY,
beneficiary_id INT NOT NULL,
item_id INT NOT NULL,
quantity INT NOT NULL CHECK (quantity >0),
distribution_date DATE NOT NULL,
FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id),
FOREIGN KEY (item_id) REFERENCES items(item_id)
);

# Inserting mock data for each table 

INSERT INTO donors 
(donor_type, donor_name, contact_person, email_address, phone_number, address)
VALUES
('private donor', 'John Doe', NULL, 'john.doe@example.com', '123-456-7890', '123 Elm Street'),
('private donor', 'Jane Smith', NULL, 'jane.smith@example.com', '987-654-3210', '456 Oak Avenue'),
('government entity', 'City Food Bank', 'Mary Johnson', 'mary.johnson@cityfoodbank.org', '555-123-4567', '789 Pine Road'),
('private donor', 'Emily Davis', NULL, 'emily.davis@example.com', '444-555-6666', '321 Birch Boulevard'),
('government entity', 'State Relief Agency', 'Robert Brown', 'robert.brown@stateagency.gov', '222-333-4444', '101 Maple Street'),
('private donor', 'Michael Wilson', NULL, 'michael.wilson@example.com', '666-777-8888', '202 Cherry Lane'),
('private donor', 'Sarah Martinez', NULL, 'sarah.martinez@example.com', '999-888-7777', '303 Cedar Drive'),
('government entity', 'County Support Services', 'Laura White', 'laura.white@countyservices.org', '111-222-3333', '404 Walnut Way');

INSERT INTO beneficiaries 
(first_name, last_name, address, phone_number, email_address, family_size)
VALUES
('Alice', 'Green', '101 Hope Street', '555-987-6543', 'alice.green@example.com', 4),
('David', 'Blue', '202 Sunshine Avenue', '555-765-4321', 'david.blue@example.com', 3),
('Nancy', 'Red', '303 Outreach Road', '555-876-5432', 'nancy.red@example.com', NULL),
('Peter', 'Yellow', '404 Assistance Lane', '555-654-3210', 'peter.yellow@example.com', 2),
('George', 'Purple', '505 Faith Boulevard', '555-543-2109', 'george.purple@example.com', NULL),
('Chris', 'Orange', '606 Helping Street', '555-432-1098', 'chris.orange@example.com', 1),
('Karen', 'Pink', '707 Future Road', '555-321-0987', 'karen.pink@example.com', 4),
('Betty', 'Brown', '808 Hope Avenue', '555-210-9876', 'betty.brown@example.com', 3);


INSERT INTO categories 
(category_name)
VALUES
('canned goods'),
('fresh products'),
('dairy products'),
('beverages'),
('adult clothing'),
('kids clothing'),
('personal care'),
('snacks'),
('frozen foods'),
('school supplies');

INSERT INTO donations 
(quantity, donation_date, donor_id)
VALUES
(20, '2024-05-01', 1),
(30, '2024-05-03', 2),
(50, '2024-05-05', 3),
(18, '2024-05-07', 4),
(70, '2024-05-09', 5),
(23, '2024-05-11', 6),
(30, '2024-05-13', 7),
(14, '2024-05-15', 8),
(35, '2023-11-10', 7),
(28, '2023-11-15', 8),
(40, '2023-11-20', 1),
(16, '2023-11-25', 3),
(25, '2022-11-10', 1),
(15, '2022-11-15', 2),
(20, '2022-11-20', 3);

INSERT INTO items
(item_name, category_id, quantity, expiry_date, description, donation_id)
VALUES
('Canned Beans', 1, 20, '2025-12-31', 'Box of canned beans - each can 16 oz', 1),
('Canned Tuna', 1, 20, '2026-01-15', 'Boxes of canned tuna in water - each can 5 oz', 2),
('Fresh Apples', 2, 10, '2024-06-15', 'bag of red apples - 1 lb each', 3),
('Shampoo', 7, 20, NULL, 'Bottle of shampoo - 16 oz', 4),
('Toothpaste', 7, 30, NULL, 'Tubes of toothpaste - 6 oz each', 5),
('Lettuce', 2, 15, '2024-06-05', 'Fresh lettuce head', 6),
('Milk', 3, 8, '2024-06-30', 'One gallon of whole milk', 7),
('Cheese', 3, 20, '2024-07-15', 'Block of cheddar cheese - 8 oz each', 8),
('Kids T-Shirts', 5, 16, NULL, 'Multicolor kids cotton T-shirt, sizes 5-12 yo', 1),
('Women Jeans', 5, 6, NULL, 'Women denim jeans, size L, M and XS', 2),
('Men Jacket', 5, 3, NULL, 'Man winter jackets, size XL, M and S', 3),
('Yogurt', 3, 3, '2024-07-01', 'Cup of strawberry yogurt - 6 oz each', 4),
('Notebooks', 10, 5, NULL, 'School notebooks', 5),
('Pens', 10, 12, NULL, 'Pack of 10 pens', 6),
('Pencils', 10, 15, NULL, 'Pack of 15 pencils', 7),
('Apple Juice', 4, 9, '2024-09-15', 'Bottle of apple juice - 64 oz', 8),
('Orange Juice', 4, 8, '2024-08-20', 'Bottles of orange juice - 64 oz each', 1),
('Bottled Water', 4, 30, '2025-01-01', 'Bottles of water - 16.9 oz each', 2)
;

INSERT INTO distributions 
(beneficiary_id, item_id, quantity, distribution_date)
VALUES
(1, 1, 10, '2024-06-01'),
(2, 2, 15, '2024-06-03'),
(3, 3, 20, '2024-05-05'),
(4, 4, 25, '2024-05-07'),
(5, 5, 30, '2024-06-09'),
(1, 1, 10, '2024-02-05'),
(2, 2, 15, '2024-08-10'),
(8, 15, 40, '2022-07-24'),
(1, 2, 45, '2023-01-08'),
(2, 4, 50, '2023-02-14'),
(3, 3, 20, '2024-09-15'),
(4, 4, 25, '2023-11-20'),
(5, 5, 30, '2023-12-25');


# I want to make sure that all the items from the items table will be deleted once passed the expiry date - adding not null as some items such as clothes and schoolk supplies will have NULL as expiry daye
# adding an expired item for testing purposes 
INSERT INTO items
(item_name, category_id, quantity, expiry_date, description, donation_id)
VALUES
('Canned Beans', 1, 20, '2023-12-31', 'Box of canned beans - each can 16 oz', 1);
-- # adding an expired item for testing purposes 

# make sure that the expiry date of distributed item is set as null, so that i can delete expired items in the items table without any error due to the foreign key present in the distributions table
UPDATE distributions AS d
JOIN items AS i ON d.item_id = i.item_id
SET i.expiry_date = NULL
WHERE i.expiry_date <= CURDATE();

DELETE FROM items 
WHERE expiry_date IS NOT NULL 
AND expiry_date < CURDATE();

SELECT * 
FROM items;

# When working on a marketing campaign to gain new donors, I want to inform potential new donors of the numbers of donors CFGCharity already has and mention the names, type of donor and name of representative/contact person for government entities

SELECT donor_name, donor_type, contact_person AS entity_representative
FROM donors
ORDER BY donor_name;

SELECT COUNT(*) AS total_donors
FROM donors;

# When items quantity of a certain category is lower than 20, I will send out an email to existing donors informing them that we are in need of items from that categories. In case they are interested in donating but unsure of what we need 

SELECT c.category_name, SUM(i.quantity) AS total_quantity
FROM categories c
JOIN items i ON c.category_id = i.category_id
GROUP BY c.category_id
HAVING total_quantity < 20;

# I want a report with all the donations combined with the donor information sorted by the most recent donation

SELECT d.donation_date, d.quantity AS items_received,
do.donor_name, do.donor_type
FROM donations d
INNER JOIN donors do ON d.donor_id = do.donor_id
ORDER BY donation_date DESC;

# number of donations by donors
SELECT 
d.donor_name,
COUNT(dn.donation_id) AS total_donations
FROM 
donors d
LEFT JOIN 
donations dn ON d.donor_id = dn.donor_id
GROUP BY 
d.donor_id, d.donor_name
ORDER BY 
total_donations ASC;


# Number of items RECEIVED BY YEAR AND MONTH. using the Monthname() function for easier readability 
SELECT YEAR(donation_date) AS donation_year, MONTHNAME(donation_date) AS donation_month, SUM(quantity) AS total_items_donated
FROM donations
GROUP BY YEAR(donation_date), MONTHNAME(donation_date)
ORDER BY YEAR(donation_date), MONTHNAME(donation_date);


# Keeping track of the total of items distributed and distributions made to beneficiaries by month and year 

SELECT 
YEAR(distribution_date) AS distribution_year,
MONTHNAME(distribution_date) AS distribution_month,
SUM(quantity) AS total_items_distributed,
COUNT(*) AS total_distributions
FROM 
distributions
GROUP BY 
distribution_year, distribution_month
ORDER BY 
distribution_year DESC, MONTHNAME(distribution_date);

# quick query to display the total distributions ever made by CFGCharity - could potentially be displayed on the frontpage of a website

SELECT COUNT(*) AS total_distributions
FROM distributions;

# Total of distributions received by a beneficiary 

SELECT 
b.first_name AS beneficiary_first_name,
b.last_name AS beneficiary_last_name,
SUM(d.beneficiary_id) AS distributions_received 
FROM distributions d
JOIN beneficiaries b ON d.beneficiary_id = b.beneficiary_id
GROUP BY b.beneficiary_id
ORDER BY b.last_name;


# This procedure will reduce the quantity of an item each time one is distributed to a beneficiary 

DELIMITER // 
CREATE PROCEDURE DistributeItem(
    IN itemID INT,
    IN distributionQuantity INT
)
BEGIN
	DECLARE remainingQuantity INT; 
    
	SELECT quantity - distributionQuantity INTO remainingQuantity
    FROM items
    WHERE item_id = itemID;
    
	IF remainingQuantity <= 0 THEN
		DELETE FROM items WHERE item_id = itemID;
    ELSE
		UPDATE items
		SET quantity = remainingQuantity
		WHERE item_id = itemID;
	END IF;
END//
DELIMITER ; 

#calling the stored function with these item and quantity - can be called with any other existing items
CALL DistributeItem(5,2);

# run this sql command to check the items table changing before and after calling the function
-- SELECT * 
-- FROM items;


#uncomment this and run it while testing
-- DROP DATABASE IF EXISTS CFGCharity;