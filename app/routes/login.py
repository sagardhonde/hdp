from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user

from app import app, bcrypt
from app.forms import LoginForm
from app.models.user import User


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if (
                user
                and user.approved
                and bcrypt.check_password_hash(user.password, form.password.data)
            ):
                login_user(user)
                next_page = request.args.get("next")
                return redirect(next_page) if next_page else redirect(url_for("index"))
            elif (
                user
                and not user.approved
                and bcrypt.check_password_hash(user.password, form.password.data)
            ):
                flash("Your account hasn't been approved yet", "info")
            else:
                flash(
                    "Login Unsuccessful. Please check username or password.", "danger"
                )
    return render_template("login.html", title="Login - HDP", form=form)
