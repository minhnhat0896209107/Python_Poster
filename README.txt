Administrator@Admin MINGW64 /d/Dev/Python/week6
$ python -m venv myenv

$ source venv/Scripts/activate
(venv) 
$ set FLASK_APP = hello_flask.py
(venv) 
$ flask run

$ pip install python-dotenv

$ pip list

$ python --version

$pip install flask-sqlalchemy flask-migrate

$  deactivate

//Sửa lỗi could not be resolved
b1. Check xem mình đang install ở folder myenv nào = lệnh 'pip uninstall flask_sqlalchemy'
b2. If (folder myenv==sai) { thì 'deactivate' } else { 'mình chịu' }
b3. đến đúng folder rồi dùng lệnh 'source myenv/Scripts/activate'



Insert row vao table
>>> from app.models import User
>>> from app import db
>>> u1 = User(username='Thanh', email='thanh@gmail.com')
>>> u1
>>> db.session.add(u1)
>>> db.session.commit()
################
Query table User
>>> User.query.all()

//create table
flask db init
flask db migrate -m "create table User"
flask db upgrade

//create table db
>>> db.create_all()


>>> from app import db
>>> db
>>> from sqlalchemy import text
>>> db.session.query(User).from_statement(text("SELECT * FROM user")).all()


//xoa 1 doi tuong 
User.query.filter_by(id = 1).delete()

//delete all
db.session.query(User).delete()
db.session.commit()