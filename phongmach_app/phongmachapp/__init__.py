from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/phongmachdb?charset=utf8mb4" % quote('Admin@123')
app.secret_key = "!@#$%^&*()"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

