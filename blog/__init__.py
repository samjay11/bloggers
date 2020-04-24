from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '102a823b12e1b6ee3445b59dc639c2c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from blog import routes
