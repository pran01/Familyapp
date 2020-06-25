from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length,ValidationError,Email,EqualTo
from familyapp.models import Users
from flask_wtf.file import FileField,FileAllowed
class LoginForm(FlaskForm):
    email=StringField('Email')
    password = PasswordField('Password',validators=[DataRequired(message='password cannot be empty'), Length(min=8, max=80)])
    remember = BooleanField('Remember me')
    login=SubmitField('Login')
    def validate_email(self,email):
        user=Users.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Username Does Not exist')


class RegisterForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(message='Name can\'t be empty'),Length(min=5,max=20)])
    email=StringField('Email')
    password=PasswordField('Password',validators=[DataRequired(message='password cannot be empty'),Length(min=8,max=80)])
    conf_password = PasswordField('Confirm Password',validators=[DataRequired(message='password cannot be empty'),
                                                                 EqualTo('password')])
    image=FileField('Profile Picture',validators=[FileAllowed(['jpg','png'])])
    register=SubmitField('Register')
    def validate_username(self,username):
        user=Users.query.filter_by(name=username.data).first()
        if user:
            raise ValidationError('Username Already Exist')

    def validate_email(self,email):
        user=Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email Already Exist')


class SendEmailForm(FlaskForm):
    message=TextAreaField('Message',validators=[DataRequired(message="Message can't be empty."),Length(min=10,max=500)])
    name=StringField('By')
    send=SubmitField('Send Mail')


class UpdateProfileForm(FlaskForm):
    name = StringField('Name')
    image = FileField('Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Submit Changes')


class UpdatePasswordForm(FlaskForm):
    name = StringField('Name')
    password = PasswordField("New Password",validators=[Length(min=8,max=80)])
    conf_password = PasswordField("Confirm Password",validators=[Length(min=8,max=80),EqualTo('password')])
    submit = SubmitField('Submit Changes')
