from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
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
    submit = SubmitField("Đăng")

class ProfileForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("password",validators = [DataRequired()])
    email = StringField("email", validators = [DataRequired()])
    address = StringField("address", validators = [DataRequired()])
    phone = StringField("phone", validators = [DataRequired()])
    submit = SubmitField("Cập nhật")


class PosterForm(FlaskForm):
    title = StringField("title", validators = [DataRequired()])   
    content = StringField("content", validators = [DataRequired()])
    image = StringField("image", validators = [DataRequired()])
    submit = SubmitField("Đăng")

class DetailForm(FlaskForm):
    idpost = StringField("idpost", validators=[DataRequired()])
    submit = SubmitField("Xem chi tiết")

class UpdatePosterForm(FlaskForm):
    idpost = StringField("idpost", validators=[DataRequired()])
    title = StringField("title", validators=[DataRequired()])
    content = StringField("content", validators=[DataRequired()])
    submit = SubmitField("Sửa")
