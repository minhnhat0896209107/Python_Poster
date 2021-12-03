from flask import render_template, redirect
import flask
from flask.wrappers import Request as request
from flask_login.utils import logout_user
from app import app
from app.forms import LoginForm, RegisterForm
from flask.helpers import flash, url_for
from app.models import Client,Poster
from flask_login import login_user, logout_user, login_required
from flask_login import  current_user
from app import  db
from flask import request
from werkzeug.urls import url_parse
import os


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    # neu user da login thi redirect den index
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect('/home')
    user = Client.query.filter_by(username=form.username.data).first()
    if user is not None:
        password = user.password
        if form.password.data == password:
            flash('Vo home roi ne')
            login_user(user)
            return redirect('/home')
    return render_template('login.html', form=form)




@app.route('/home', methods = ['GET', 'POST'])
def home():
    flash("Không có bài viết nào")
    ls = db.session.query(Client,Poster).filter(Client.id == Poster.id)
    if ls is None:
        flash("Không có bài viết nào")
    else:
        for i in ls:
            flash(i.Client.username)

    return render_template('home.html', ls = ls)




@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        passwordrp = form.passwordrp.data
        email = form.email.data
        address = form.address.data
        phone = form.phone.data
        user = Client.query.filter_by(username = username).first()
        
        if user is not None:
            flash('username is exists')
            return redirect('/register')
        else:
            if password == passwordrp:
                flash('Register success')
                flash('new username is ' + username)
                u1 = Client(username= username, password=password, email = email, address = address, phone = phone)
                db.session.add(u1)
                db.session.commit()
                return redirect('/login')
            else:
                flash('password different passwordrp')
                return redirect('/register')
    return render_template('register.html', form=form)

        
@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect('/login')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods = ['POST'])
def upload_file():
    upload_file = request.files['file']
    if upload_file.filename != '':
        # upload_file.save("static/" + upload_file.filename)
        upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'], upload_file.filename))
    return redirect('/index')