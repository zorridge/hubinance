# Flask app set up courtesy of CS50 staff
# https://cs50.harvard.edu/x/2022/psets/9/finance/

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

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


# Homepage
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Query for necessary data
    portfolio = []
    holdings = db.execute("SELECT symbol, shares FROM holdings WHERE id = ?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    total = cash

    for row in holdings:
        holding = {}
        holding["symbol"] = row["symbol"]
        holding["name"] = lookup(row["symbol"])["name"]
        holding["shares"] = row["shares"]
        holding["price"] = lookup(row["symbol"])["price"]
        holding["total"] = holding["price"] * row["shares"]
        total += holding["total"]
        portfolio.append(holding)

    return render_template("index.html", portfolio=portfolio, cash=cash, total=total)


# Buy stock
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        shares = request.form.get("shares")

        # Validate symbol
        if not quote:
            return apology("symbol does not exist", 400)

        if not shares.isdigit():
            return apology("shares must be a positive integer", 400)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = quote["price"]*float(shares)

        # Check for user's cash balance and if user can afford purchase
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if total > cash:
            return apology("insufficient cash", 400)

        # Update transactions table
        db.execute("INSERT INTO transactions (symbol, type, name, shares, price, total, time, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   quote["symbol"], "buy", quote["name"], shares, quote["price"], total, now, session["user_id"])

        # Update holdings table
        holdings = db.execute("SELECT symbol, shares FROM holdings WHERE id = ? and SYMBOL = ?",
                              session["user_id"], quote["symbol"])

        if not holdings:
            db.execute("INSERT INTO holdings (id, symbol, shares) VALUES (?, ?, ?)", session["user_id"], quote["symbol"], shares)
        else:
            db.execute("UPDATE holdings SET shares = ? WHERE id = ? AND SYMBOL = ?",
                       holdings[0]["shares"] + int(shares), session["user_id"], quote["symbol"])

        # Update user's cash balance
        cash = cash-total
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        # Redirect to portfolio homepage
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


# Transaction history
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Query for transaction data
    transactions = db.execute("SELECT symbol, type, shares, price, time FROM transactions WHERE user_id = ?", session["user_id"])
    return render_template("history.html", transactions=transactions)


# Login
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


# Logout of web app
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# Quote price given a ticker
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if not request.form.get("symbol"):
            return apology("missing symbol")
        elif not quote:
            return apology("invalid symbol")
        else:
            return render_template("quoted.html", quote=quote)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


# Register new account
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure inputs were submitted
        if not username or not password or not confirmation:
            return apology("insufficient input", 400)

        # Validate username
        if db.execute("SELECT username FROM users WHERE username = ?", username):
            return apology("username already exists", 400)

        # Validate password
        if password != confirmation:
            return apology("passwords do not match", 400)

        # Populate finance.db
        hashed = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed)

        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


# Sell stock
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Query for user data
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        shares = request.form.get("shares")
        holdings = db.execute("SELECT symbol, shares FROM holdings WHERE id = ? AND symbol = ?",
                              session["user_id"], quote["symbol"])

        # Validate sale
        if not holdings:
            return apology("stock not owned", 400)

        if not symbol:
            return apology("no stock selected", 400)

        if not shares.isdigit():
            return apology("shares must be a positive integer", 400)

        if int(shares) > holdings[0]["shares"]:
            return apology("insufficient shares owned", 400)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = quote["price"]*float(shares)

        # Update transactions table
        db.execute("INSERT INTO transactions (symbol, type, name, shares, price, total, time, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   quote["symbol"], "sell", quote["name"], shares, quote["price"], total, now, session["user_id"])

        # Update holdings table
        db.execute("UPDATE holdings SET shares = ? WHERE id = ? AND SYMBOL = ?",
                   holdings[0]["shares"] - int(shares), session["user_id"], quote["symbol"])

        # Update user's cash balance
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]+total
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        # Redirect to portfolio homepage
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Query for user's holdings
        holdings = db.execute("SELECT symbol, shares FROM holdings WHERE id = ?", session["user_id"])
        return render_template("sell.html", holdings=holdings)
