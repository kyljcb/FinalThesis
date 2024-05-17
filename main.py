import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='192.168.1.127',  # IP address of your Windows laptop
            user='puphas',
            password='Puphas-2024',
            database='puphas'  # Name of your database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO subjects (subject_code, subject_name) VALUES ('RASPITEST01', 'Inserted Using Raspberry Pi')")
        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        insert_data(conn)
        conn.close()
