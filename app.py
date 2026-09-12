from flask import Flask, render_template, request,session,redirect
from db import get_db_connection
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recharge", methods=["GET", "POST"])
def recharge():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        mobile = request.form["mobile"]
        operator=request.form["operator"]
        amount = request.form["amount"]
        user_id=session["user_id"]
        connection=get_db_connection()
        cursor=connection.cursor()
        sql="""INSERT INTO recharges(mobile,operator,amount,user_id)
        values(%s,%s,%s,%s)"""
        values=(mobile,
                operator,
                amount,
                user_id)
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        connection.close()
        return render_template("successrecharge.html")


    return render_template("recharge.html")


@app.route("/bills",methods=["POST","GET"])
def bills():
    if "user_id" not in session:
        return redirect("/login")
        
    if request.method=="POST":
        customer_name=request.form["customer_name"]
        bill_number=request.form["bill_number"]
        bill_type=request.form["bill_type"]
        Amount=request.form["amount"]
        user_id =session["user_id"]

        connection=get_db_connection()
        cursor=connection.cursor()
        sql="""
            INSERT INTO transactions
            (customer_name,bill_number,bill_type,Amount,user_id)
            values(%s,%s,%s,%s,%s)
            """
        values=(customer_name,
                bill_number,
                bill_type,
                Amount,
                user_id)
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        connection.close()
        return render_template("successbills.html")
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
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        db=get_db_connection()
        cursor=db.cursor()
        sql="""select id,name from users 
        where email=%s and password=%s"""
        values=(email,password)
        cursor.execute(sql,values)
        user=cursor.fetchone()
        cursor.close()
        db.close()
        if user:
            session["user_id"]=user[0]
            session["user_name"]=user[1]
            return render_template("dashboard.html")
        else:
            return "Invalid email or password"
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
@app.route("/history")
def history():
    if "user_id" not in session:
        return "please login first"
    return render_template("history.html")
@app.route("/history/bills")
def historybills():
    if "user_id" not in session:
        return"Please Login first"
    user_id=session["user_id"]
    connection=get_db_connection()
    cursor=connection.cursor()
    sql="""select bill_number,bill_type,Amount from transactions 
    where user_id=%s"""
    values=(user_id,)
    cursor.execute(sql,values)
    transactions=cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("history_bills.html",
                           transactions=transactions,history_type="Bills")

@app.route("/history/recharges")
def history_recharges():
    if "user_id" not in session:
        return "please login first"
    user_id=session["user_id"]
    connection=get_db_connection()
    cursor=connection.cursor()
    sql="""select mobile,operator,amount from recharges
    where user_id=%s"""
    values=(user_id,)
    cursor.execute(sql,values)
    transactions=cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("history_recharges.html",transactions=transactions,
                           history_type="Recharges")

@app.route("/about")
def about():
    return render_template("about.html")

app.secret_key = "akRiva_secret_key_2026"
app.run(debug=True)