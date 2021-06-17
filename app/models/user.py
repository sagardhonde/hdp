from flask_login import UserMixin

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    u_type = db.Column(db.String(10), nullable=False)
    approved = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"User( Id : {self.id}, Email : {self.email}, User Type : {self.u_type}, Approved : {self.approved})"
