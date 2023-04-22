import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from datetime import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    transactions = db.execute(
        "SELECT symbol, name, SUM(shares) AS shares, price FROM transactions WHERE user_id = ? GROUP BY symbol", session["user_id"])
    account = cash[0]["cash"]

    for transaction in transactions:
        name = transaction["name"]
        total = transaction["shares"] * transaction["price"]
        transaction["name"] = name
        transaction["total"] = total
        transaction["price"] = transaction["price"]
        account += total
    return render_template("index.html", transactions=transactions, cash=cash[0]["cash"], account=account)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol")

        quote = lookup(symbol)
        if not quote:
            return apology("invalid symbol")

        shares = request.form.get("shares")
        if not shares:
            return apology("missing shares")

        if not shares.isdigit():
            return apology("invalid shares")

        shares = int(shares)
        if shares <= 0:
            return apology("invalid shares")

        row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = row[0]["cash"]
        balance = cash - (shares * quote["price"])
        if balance < 0:
            return apology("can't afford")

        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, name, price, transacted) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol.upper(), shares, quote["name"], quote["price"], datetime.now())
        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute(
        "SELECT symbol, shares, name, price, transacted FROM transactions WHERE user_id = ?", session["user_id"])
    if not transactions:
        return apology("no history", 403)
    else:
        return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol")

        quote = lookup(symbol)
        if not quote:
            return apology("invalid symbol")

        return render_template("quoted.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        if not name or db.execute("SELECT * FROM users WHERE username = ?", name):
            return apology("username is not available")

        password = request.form.get("password")
        if not password:
            return apology("missing password")

        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("missing confirmation")

        if password != confirmation:
            return apology("passwords don't match")

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, generate_password_hash(password))
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol")

        shares = request.form.get("shares")
        if not shares:
            return apology("missing shares")

        shares = int(shares)
        if (shares <= 0):
            return apology("shares must be positive")

        sumshares = db.execute(
            "SELECT symbol, price, name, SUM(shares) AS shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        if (shares > sumshares[0]["shares"]):
            return apology("too many shares")

        db.execute("INSERT INTO transactions (user_id, symbol, shares, name, price, transacted) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol.upper(), -shares, sumshares[0]["name"], sumshares[0]["price"], datetime.now())

        sold = shares * sumshares[0]["price"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + sold, session["user_id"])
        flash("Sold!")
        return redirect("/")
    else:
        symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", session["user_id"])
        return render_template("sell.html", symbol=symbols)


@app.route("/addcash", methods=["GET", "POST"])
@login_required
def addcash():
    """User can add additional cash to their account"""
    if request.method == "POST":
        add_cash = request.form.get("add_cash")
        if not add_cash:
            return apology("missing add cash")

        add_cash = int(add_cash)
        if add_cash <= 0:
            return apology("add cash must be positive")

        row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = row[0]["cash"]
        balance = cash + add_cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"])
        flash("Added!")
        return redirect("/")
    else:
        return render_template("addcash.html")
