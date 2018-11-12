
from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, TransactionForm
from app.models import User, Transaction

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    transactions = Transaction.query.all()
    return render_template('index.html', title='Home', users=users, transactions=transactions)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	flash("Login requested for user {}, remember_me={}".format(
    			form.username.data, form.remember_me.data))
    	return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/transaction', methods=['GET','POST'])
def transaction():
    form = TransactionForm()
    if form.validate_on_submit():
    	transaction = Transaction(due_date=form.due_date.data, amount=float(form.amount.data),
    								description=form.description.data, user=int(form.user.data))
    	db.session.add(transaction)
    	db.session.commit()
    	flash("Transaction {}, of amount {} registered".format(
    			form.description.data, form.amount.data))
    	return redirect(url_for('index'))
    return render_template('transaction.html', title='Transaction', form=form)




