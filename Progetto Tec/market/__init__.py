from flask import Flask, render_template
from market import routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '0878cc8ae6fae32b31b9cc89'
db = SQLAlchemy(app)

