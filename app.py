from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recharge", methods=["GET", "POST"])
def recharge():

    if request.method == "POST":

        mobile = request.form["mobile"]
        amount = request.form["amount"]

        print("Mobile:", mobile)
        print("Amount:", amount)

    return render_template("recharge.html")


@app.route("/bills")
def bills():
    return render_template("bills.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug=True)