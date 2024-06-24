# Car-management-system
Car Rental Website Project This project aims to create a user-friendly platform for renting cars online. Our website simplifies the car rental process by offering an intuitive interface for browsing, selecting, and booking vehicles from a diverse fleet.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

XAMPP is required to run the project.
The project will be hosted on a localhost server.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Installation*
Install XAMPP.
Open XAMPP and click on the Start button.
Clone the project to the root of the XAMPP server.
Open the project in XAMPP.
Import SQL file from database folder to the XAMPP server.
Open Browser and navigate to localhost:8080.
Hurray! The project is now running.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Database*
The database is stored in a folder called database.
The database is named as carproject.sql.
The database is stored in the root of the XAMPP server.
The database is imported to the XAMPP server.
Database used is MySQL.
Database Connection page is named connection.php.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


*TABLE*
The table is named as car.
The table has the following columns:
car_id: INTEGER PRIMARY KEY AUTO_INCREMENT
car_make: VARCHAR(255)
car_model: VARCHAR(255)
car_year: INTEGER
car_color: VARCHAR(255)
car_price: INTEGER
car_available: BOOLEAN
car_image: VARCHAR(255)
car_description: VARCHAR(255)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


*Car Listing Page*
The car listing page will have a search bar and a car listing table.
The search bar will have a search button.
The search button will search for the car based on the search bar input.
The car shown only on the car listing page will be the car that is available.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


*User Story*
As a user, I want to be able to search for a car.
As a user, I want to be able to see the car that is available.
As a user, I want to be able to reserve a car.
As a user, I want to be able to return a car.
As a user, I want to be able to see the car that I have reserved.
As a user, I want to provide feedback to the car rental website.
As a user, I should be able to make payment for the car rental.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

