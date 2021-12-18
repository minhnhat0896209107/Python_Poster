from flask import render_template, redirect,session
import flask 
from flask.wrappers import Request as request
from flask_login.utils import logout_user
from sqlalchemy.orm import session
from wtforms.fields.simple import SubmitField
from app import app
from app.forms import DetailForm, UpdatePosterForm, LoginForm, PosterForm, ProfileForm, RegisterForm, CommentForm
from flask.helpers import flash, url_for
from app.models import Client, Comment,Poster
from flask_login import login_user, logout_user, login_required
from flask_login import  current_user
from app import  db
from flask import request, session
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

@app.route('/detail' ,methods = ['GET', 'POST'])
def detail():
    formdt = UpdatePosterForm()

    if 'idpost' in session:
        idpost = session['idpost']
        p = Poster.query.filter_by(id = idpost).first()
        print(p.title + " " + p.content)
    print("trc btn")
    if formdt.validate_on_submit():  
        print('click btn 11')
    
    return render_template('detail.html', p = p, formdt = formdt)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    form = ProfileForm()
    formdetail = DetailForm()
    if current_user.is_authenticated:
        user = Client.query.filter_by(id=current_user.get_id()).first()
        ls1 = db.session.query(Poster,Client).filter(Poster.client_id == current_user.get_id(),Client.id == Poster.client_id)

    
    if form.validate_on_submit():
        id = current_user.get_id()
        email = form.email.data
        username = form.username.data
        address = form.address.data
        phone = form.phone.data
        password = form.password.data

        print (id + " " + email + " " + username + " " + address + " " + password +  " " + phone)
        client = Client.query.filter_by(id = id).first()
        client.username = username
        client.email = email
        client.address = address
        client.password = password
        client.phone = phone
        db.session.commit()
    if formdetail.validate_on_submit():
        idpost = formdetail.idpost.data
        if request.method == 'POST':
            session['idpost'] = idpost
            return redirect(url_for('detail'))
        print("id =" + idpost)
        print("vo day roi ne hehe")
    return render_template('profile.html', user = user, form = form, formdetail = formdetail, ls1 = ls1)

@app.route('/poster', methods = ['GET', 'POST'])
def poster():
    form = PosterForm()
    if current_user.is_authenticated:
        user = Client.query.filter_by(id=current_user.get_id()).first()
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            image = form.image.data
            id = current_user.get_id()
            print( id + "   " + title + "   " + content + "    "  + image) 
            p = Poster(title= title, content=content, image = image, client_id =id, number_like = 217)
            db.session.add(p)
            db.session.commit()
            return redirect('/home')        

    return render_template('poster.html',user = user, form = form)


@app.route('/home', methods = ['GET', 'POST'])
def home():
   
    flash("Không có bài viết nào")
    ls = db.session.query(Client,Poster).filter(Client.id == Poster.client_id)
    ls_cmt = db.session.query(Client,Poster,Comment).filter(Client.id == Comment.client_id).filter(Comment.post_id == Poster.id)

    if ls is None:
        flash("Không có bài viết nào")
    else:
        for i in ls:
            flash(i.Client.username)
    user = "Chưa đăng nhập"
    if current_user.is_authenticated:
        user = Client.query.filter_by(id=current_user.get_id()).first()
    form = CommentForm()
    if form.validate_on_submit():
        print(form.content.data)
        print(user.id)
        print(form.getpost_id.data)
        id_client = user.id
        id_post = form.getpost_id.data
        content = form.content.data
        form.content.data = ''
        cmt = Comment(client_id=id_client,post_id=id_post,content = content)
        db.session.add(cmt)
        db.session.commit()
    return render_template('home.html', ls = ls,ls_cmt = ls_cmt,user = user,form = form)



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