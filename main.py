#!/usr/bin/python3
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

from app import app

app.wsgi_app = ProxyFix(app.wsgi_app)
	 
if __name__ == '__main__':
    app.run()



