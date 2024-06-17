"""Script entry point."""

from flask import Flask, render_template, request, session, url_for, redirect
from controllers.client_controller import *
from logger import LOGGER


app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/do_login', methods=['POST'])
def do_login():
    identifiant = request.form.get("identifiant")
    pin = request.form.get("pin")
    user = login_customer(identifiant, pin)
    if(user):
        session['identifiant'] = identifiant
        session['pin'] = pin
        return(redirect(url_for("list_users_page")))
    else:
        return render_template("login.html", error_login = True)

@app.route('/list_users_page', methods=['GET'])
def list_users_page():
    if (session['identifiant'] is None):
        return(redirect(url_for("login")))
    users = list_users()
    return render_template("list_users.html", users = users)

@app.route('/list_transaction_page', methods=['GET'])
def list_transaction_page():
    if (session['identifiant'] is None):
        return(redirect(url_for("login")))
    trxs = list_all_transactions()
    return render_template("list_trxs.html", trxs = trxs)

@app.route('/transaction_page', methods=['GET'])
def transaction_page():
    if (session['identifiant'] is None):
        return(redirect(url_for("login")))
    users = list_users()
    return render_template("transaction.html", users = users)

@app.route('/do_transaction_form', methods=['POST'])
def do_transaction_form():
    if (session['identifiant'] is None):
        return(redirect(url_for("login")))
    transaction_solde = do_transaction_flask(request.form.get("compte_emmeteur"), int(request.form.get("amount")), request.form.get("compte_recepteur"))
    
    if(transaction_solde.login_done):
        if(transaction_solde.transfert_done):
            print(transaction_solde.message_transfert + "\n")
            return(redirect(url_for("list_transaction_page")))
        else:
            print(transaction_solde.message_transfert + "\n")
            return(redirect(url_for("transaction_page")))
    else:
        print(transaction_solde.message_login + "\n")
        return(redirect(url_for("login")))

@app.route("/logout")
def logout():
    session.pop("identifiant", None)
    session.pop("pin", None)
    return(redirect(url_for("login")))

if __name__ == "__main__":
    app.secret_key = 'my_secret'
    LOGGER.remove()
    app.run(debug=True, host="0.0.0.0", port=8080)