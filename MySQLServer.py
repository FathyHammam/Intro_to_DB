import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (update user and password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Change to your MySQL username
            password="yourpassword"  # Change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
