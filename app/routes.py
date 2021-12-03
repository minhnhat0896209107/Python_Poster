from flask import render_template, redirect
import flask
from flask.wrappers import Request as request
from flask_login.utils import logout_user
from app import app
from app.forms import LoginForm, RegisterForm
from flask.helpers import flash, url_for
from app.models import Client
from flask_login import login_user, logout_user, login_required
from flask_login import  current_user
from app import  db
from flask import request
from werkzeug.urls import url_parse
import os

# @app.route('/')
# @app.route('/index')
# @login_required
# def index():
#     users = [
#         {'id': 'u01','name':'Nathan'},
#         {'id': 'u02','name':'Nathan Nguyen'},
#         {'id': 'u03','name':'Nevermore'}
#         ]
#     return render_template('index.html', users=users)

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    # neu user da login thi redirect den index
    form = LoginForm()

    if form.validate_on_submit():
        # Kiem tra user co trong db hay khong
        # Thong tin user lay tu form: form.username.data
        # user = Client.query.filter_by(email=form.username.data).first()

        # if user is not None:
        #     password = user.password
        #     flash('Vo home roi ne')
        #     if form.password.data == password:
        #     # Kiem tra password co khop khong
        #         return redirect(url_for('/home'))
        #     else:
        #         return redirect('/login')
        # else:
        #     flash('Login fail')
        #     return render_template('login.html', form = form)
        # flash('Login of user {}'.format(form.username.data))
        # login_user(user)

        #xu ly next
        # next_page = request.args.get('next')
        # if next_page is not None:
        #     flash('Next page {}'.format(next_page))
        #     if url_parse(next_page).netloc != '':
        #         flash('netloc ' + url_parse(next_page).netloc)
        #         next_page = '/index'
        # else:
        #     next_page = '/index'
        # return redirect(next_page)
        return redirect('/home')
    return render_template('login.html', form=form)

@app.route('/home', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

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

        
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

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