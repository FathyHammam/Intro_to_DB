import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establishing the connection to MySQL server
        db_connection = mysql.connector.connect(
            host="localhost",        # You can change this if your MySQL server is hosted elsewhere
            user="root",             # Your MySQL username
            password="your_password" # Your MySQL password
        )

        cursor = db_connection.cursor()

        # Check if database already exists before creating it
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied. Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Ensure the database connection is closed properly
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    create_database()
