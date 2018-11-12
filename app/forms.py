from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, DecimalField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	"""docstring for LoginForm"""
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class TransactionForm(FlaskForm):
	"""docstring for TransactionForm"""
	due_date = DateField('Due Date', format='%d/%m/%Y',validators=[DataRequired()])
	amount = DecimalField('Amount', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	user = IntegerField('User ID', validators=[DataRequired()])
	submit = SubmitField('Log Transaction')