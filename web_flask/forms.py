#!/usr/bin/python3
"""
Get user inputs using flask wtf
"""
from models import storage
from models.user import User
from models.parcel import Parcel


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class RegistrationForm(FlaskForm):
    """registration form"""
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = TelField('Phone number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


    def validate_username(self, username):
        '''validation check'''
        if storage.is_available(User, "username", username.data):
            raise ValidationError("Username exists, choose a different one")

    def validate_email(self, email):
        '''validation check'''
        if storage.is_available(User, "email", email.data):
            raise ValidationError("Entered email already registered.")



class LoginForm(FlaskForm):
    """login form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')



class SearchForm(FlaskForm):
    """search form"""
    origin = StringField('Origin', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    submit = SubmitField('Search')



class ParcelForm(FlaskForm):
    '''register parcel'''
    origin = StringField('Origin', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    size_l_cm = DecimalField('Size length cm', validators=[DataRequired()])
    size_w_cm = DecimalField('Size width (cm)', validators=[DataRequired()])
    size_h_cm = DecimalField('Size height (cm)', validators=[DataRequired()])
    weight_kg = DecimalField('Weight (kg)', validators=[DataRequired()])
    offered_amount = DecimalField('Amount offered (KES)', validators=[DataRequired()])
    submit = SubmitField('Post')
