from app import db
from app import login
from flask_login import UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,unique=True)
    email = db.Column(db.String(120), index=True,unique=True)
    role = db.Column(db.String(24))
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User> {}'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(200)) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post> {}'.format(self.body)

class Client(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(30), index=True)
    address = db.Column(db.String(120), index=True)
    phone = db.Column(db.String(11), index=True)

class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    content = db.Column(db.String(1000), index=True)
    image = db.Column(db.String(100), index=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    number_like = db.Column(db.Integer)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('poster.id'))
    content = db.Column(db.String(1000), index=True)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))