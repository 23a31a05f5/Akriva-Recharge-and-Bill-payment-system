import mysql.connector
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kal@admin@sql#0830",
        database="akriva"
    )

    return connection
connection = get_db_connection()

if connection.is_connected():
    print("MySQL connected successfully!")

connection.close()