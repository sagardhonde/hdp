from flask import flash, redirect, render_template, request, url_for

from app import app, bcrypt, db
from app.forms import RegistrationForm
from app.models.user import User


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_passwd = bcrypt.generate_password_hash(form.password.data).decode(
                "UTF-8"
            )
            user = User(
                email=form.email.data.lower(),
                u_type=form.u_type.data.lower(),
                password=hashed_passwd,
                approved=1,
            )
            db.session.add(user)
            db.session.commit()
            flash("Your Account has been created successfully!", "success")
            return redirect(url_for("login"))
    return render_template("register.html", title="Register - HDP", form=form)
