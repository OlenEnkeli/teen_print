from app import db
from app import login
from flask_login import UserMixin
from datetime import datetime
import hashlib
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
	def check_password(self, password):
		if self.password == hashlib.sha256(password.encode('utf8')).hexdigest():
			return True
		else:
			return False
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(100), index=True)
	password = db.Column(db.String(100))
	first = db.Column(db.Integer)
	secret = db.Column(db.String(100))
	posts = db.relationship('Msg', backref='belongs_to', lazy='dynamic')
	
class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.String(140))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    

