# contain forms required for user interaction

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField, FileRequired


class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2)])
    password1 = PasswordField('Enter your password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm your password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New password', validators=[DataRequired(), Length(min=6)])
    change_password = SubmitField('Change Password')


class ShopItemsForm(FlaskForm):
    product_name = StringField('Name of product', validators=[DataRequired()])
    current_price = FloatField('Current price', validators=[DataRequired()])
    previous_price = FloatField('Previous price', validators=[DataRequired()])
    in_stock = IntegerField('In stock', validators=[DataRequired(), NumberRange(min=0)])
    product_picture = FileField('Product Picture', validators=[FileRequired()])
    flash_sale = BooleanField('Flash Sale')

    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update')


class OrderForm(FlaskForm):
    order_status = SelectField('Order status', choices=[('pending', 'pending'), ('accepted', 'accepted'),
                                                        ('out for delivery', 'out for delivery'),
                                                        ('delivered', 'delivered'), ('cancelled', 'cancelled')])
    update = SubmitField('Updated status')