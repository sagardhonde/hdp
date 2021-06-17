import re

from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from app.models.user import User


class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    u_type = SelectField(
        label="Type", choices=[("patient", "patient"), ("doctor", "doctor")]
    )
    # u_type = RadioField("User Type", validators=[DataRequired()], choices=[("doctor", "doctor"), ("patient", "patient")])
    submit = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Account for this email is already created.")

    def validate_password(self, password):
        r = re.compile(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"
        )
        if not r.match(password.data):
            raise ValidationError(
                "Password should be 8-20 char long with one upper, one lower, one numerical and one special character"
            )
