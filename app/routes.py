from flask_login import current_user, login_user
from flask import render_template,flash,redirect,request
from app import app,forms,models,db
from app.models import User
from flask_login import logout_user
@app.route('/')
def index_page():
	form = forms.LoginForm()
	print(current_user.is_authenticated)
	if current_user.is_authenticated:
		
		return render_template('index.html',title='Главная',form=form,noauto = False)
	else:
		return render_template('index.html',title='Главная',form=form,noauto = True)

mails = [{ 'msg' :'Принтер прекратил работу','data':'10.02.2392'},
	{'msg' :'Работа закончена','data':'30.02.2392'}]	
@app.route('/login', methods=['POST'])
def login_page():
	form = forms.LoginForm()
	if form.validate_on_submit():
		print(form.login.data, form.password.data)
		user = User.query.filter_by(login=form.login.data).first()
		print(user is None)
		if user is None or not user.check_password(form.password.data):
			flash('Invalid logon or password')
			return render_template('index.html',
			title='Вход',form=forms.LoginForm(),denied = True,noauto = True)
		#Сверка с базой данных
		login_user(user, remember=form.remember_me.data)
		return redirect('/mail')
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')
	

@app.route('/logout')
def logout_page():	
	return None
	
@app.route('/mail')
def static_page():  
	return render_template('mail.html',posts = mails)
	
	
@app.route('/test')
def test():
	u = User(login='a',password='a',first=False)
	db.session.add(u)
	db.session.commit()
	return "hello"


