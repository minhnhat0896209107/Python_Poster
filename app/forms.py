from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("password", validators = [DataRequired()])
    submit = SubmitField("Sign in")

class RegisterForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("password",validators = [DataRequired()])
    passwordrp = PasswordField("passwordrp", validators = [DataRequired()])
    email = StringField("email", validators = [DataRequired()])
    address = StringField("address", validators = [DataRequired()])
    phone = StringField("phone", validators = [DataRequired()])
    submit = SubmitField("Registser")

class CommentForm(FlaskForm):
    content = StringField("content", validators = [DataRequired()])
    getpost_id = StringField("getpost_id", validators = [DataRequired()])
    submit = SubmitField("đăng")