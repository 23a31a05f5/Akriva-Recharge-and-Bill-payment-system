from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recharge")
def recharge():
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