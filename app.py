from flask import Flask, render_template, request
from db import get_db_connection
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recharge", methods=["GET", "POST"])
def recharge():

    if request.method == "POST":

        mobile = request.form["mobile"]
        amount = request.form["amount"]
        connection=get_db_connection()
        cursor=connection.cursor()
        sql="""INSERT INTO recharge(mobile,amount)
        values(%s,%s)"""
        values=(mobile,
                amount)
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        connection.close()
        print("Recharge history updated")


    return render_template("recharge.html")


@app.route("/bills",methods=["POST","GET"])
def bills():
    if request.method=="POST":
        customer_name=request.form["customer_name"]
        bill_id=request.form["bill_id"]
        bill_type=request.form["bill_type"]
        Amount=request.form["amount"]

        connection=get_db_connection()
        cursor=connection.cursor()
        sql="""
            INSERT INTO transactions
            (customer_name,bill_id,bill_type,Amount)
            values(%s,%s,%s,%s)
            """
        values=(customer_name,
                bill_id,
                bill_type,
                Amount)
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        connection.close()
        print("Bill payment successful")
    return render_template("bills.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]

        connection=get_db_connection()
        cursor=connection.cursor()
        sql="""INSERT into users(name,email,password)
        values(%s,%s,%s)
        """
        values=(name,email,password)
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        connection.close()
        return render_template("successregister.html")
    return render_template("register.html")
@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug=True)