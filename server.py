from flask import Flask
from flask_oauthlib.provider import OAuth2Provider
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
oauth = OAuth2Provider(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

