from flask import Flask
from db import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to BillEase"


@app.route("/users")
def users():

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")

    users_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return users_data


if __name__ == "__main__":
    app.run(debug=True)