from app import db
from datetime import datetime

class User(db.Model):
	"""docstring for User"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	transactions = db.relationship('Transaction', backref='owner', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	due_date = db.Column(db.DateTime, index=True)
	amount = db.Column(db.Float)
	description = db.Column(db.String)
	manual_entry_flag = db.Column(db.Boolean)
	user = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Transaction {}>'.format(self.description)