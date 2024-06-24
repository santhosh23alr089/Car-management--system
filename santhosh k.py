import mysql.connector

# Establishing the connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

def insert_customer_detail():
    # Collecting details from user input
    details = {
        'car_name': input("Car Name: "),
        'address': input("Address: "),
        'registration_no': input("Registration No: "),
        'licence_no': input("Licence No: "),
        'car_type': input("Type of car (No of seats): "),
        'rental_date': input("Rental date: "),
        'drop_date': input("Drop date: ")
    }
    
    # SQL query to insert details into the customer_details table
    sql = """
        INSERT INTO customer_details (
            car_name, 
            address, 
            registration_no, 
            licence_no, 
            car_type, 
            rental_date, 
            drop_date
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    # Values to be inserted
    values = (
        details['car_name'], 
        details['address'], 
        details['registration_no'], 
        details['licence_no'], 
        details['car_type'], 
        details['rental_date'], 
        details['drop_date']
    )
    
    # Executing the SQL query
    mycursor = mydb.cursor()
    mycursor.execute(sql, values)
    
    # Committing the transaction
    mydb.commit()
    
    print("Customer details inserted successfully.")
def display_customer_details():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM customer_details"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    # Displaying the results
    for row in result:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Address:", row[2])
        print("Registration No:", row[3])
        print("License No:", row[4])
        print("Car Type:", row[5])
        print("Rental Date:", row[6])
        print("Drop Date:", row[7])
        print("-" * 40)
while True:
    print("Menu:")
    print("1. Insert Data")
    print("2. Display Data")
    print("3. Exit")
    choice = int(input('Enter Choice: '))
    match choice:
        case 1:
            insert_customer_detail()
        case 2:
            display_customer_details()
        case 3 :
            print('Exited....')
            break
        case _:
            print("Invaild choice")
             