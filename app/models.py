from app import db
from app import login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin,db.Model):
	def check_password(self, password):
		if self.password == password:
			return True
		else:
			return False
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(100), index=True)
	password = db.Column(db.String(100))
	first = db.Column(db.Integer)
	

