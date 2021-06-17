import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .config import ADMIN_EMAIL, ADMIN_PASSWD, DATABASE_NAME, SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "login"
login_manager.login_message = "You need to be logged in to view this page"
login_manager.login_message_category = "danger"

from app import routes
from app.models import User

if not os.path.isfile(os.path.join(os.getcwd(), "app", DATABASE_NAME + ".db")):
    db.create_all()
    master_user = User(
        email=ADMIN_EMAIL,
        password=bcrypt.generate_password_hash(ADMIN_PASSWD),
        u_type="admin",
        approved=True,
    )
    db.session.add(master_user)
    db.session.commit()
