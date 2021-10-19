from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length, Email, EqualTo, ValidationError, Regexp, InputRequired
from onlineshop.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired(),Length(min=3,max=15)])
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired(),Regexp('^.{6,15}$',message='Your password should between 6 and 15 characters long.'), Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,15}$", message='Your password must contain at least one number'),Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,15}$", message="Password must contain at least one upper and one lower case")])
  confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Username already exist. Please choose a different one.')

  def validate_email(self,email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Email address is already associated with an account.')

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

class CheckoutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=7,max=11)])
    card_number = StringField('Card Number', validators=[DataRequired(), Length(min=16,max=16)])
    expiry = StringField('Card Expiry', validators=[DataRequired()])
    security = StringField('Security Number', validators=[DataRequired(), Length(min=3, max=3)])
    submit = SubmitField('Checkout')

class ReviewForm(FlaskForm):
    Comment = StringField('Add Review Here: ', validators=[DataRequired(), Length(min=1, max=150)])
    submit = SubmitField('Review')
"""class CommentForm(FlaskForm):
  comment = StringField('Comment',validators=[InputRequired()])
  submit = SubmitField('Post comment')"""
