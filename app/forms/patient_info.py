from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired


class PatientInfo(FlaskForm):
    age = IntegerField(label="Age", validators=[InputRequired()])
    gender = SelectField(
        label="Gender",
        validators=[InputRequired()],
        choices=[(0, "Female"), (1, "Male")],
    )
    chest_pain = SelectField(
        label="Cheast Pain",
        validators=[InputRequired()],
        choices=[
            (1, "Typical Angina"),
            (2, "Atypical Angina"),
            (3, "Non-Anginal Pain"),
            (4, "Asymptotic"),
        ],
    )
    resting_bp = IntegerField(label="Resting BP (mmHg)", validators=[InputRequired()])
    sereum_cholestoral = IntegerField(
        label="Sereum Cholestoral (mg/dl)", validators=[InputRequired()]
    )
    fasting_blood_sugar = SelectField(
        label="Fasting Blood Sugur",
        validators=[InputRequired()],
        choices=[
            (0, "Less than or Equal to 120mg/dl"),
            (1, "More than 120mg/dl"),
        ],
    )
    resting_ecg = SelectField(
        label="Resting ECG",
        validators=[InputRequired()],
        choices=[
            (0, "Normal"),
            (1, "ST-T Wave Abnormality"),
            (2, "Left Ventricular Abnormality"),
        ],
    )
    max_heart_rate = IntegerField(
        label="Maximum Heart Rate", validators=[InputRequired()]
    )
    exercise_induced_angina = SelectField(
        label="Exercise Induced Angina",
        validators=[InputRequired()],
        choices=[
            (0, "Yes"),
            (1, "No"),
        ],
    )
    oldpeak = FloatField(label="Oldpeak", validators=[InputRequired()])
    slope = SelectField(
        label="Slope",
        validators=[InputRequired()],
        choices=[(1, "Upsloping"), (2, "Flat"), (3, "Downsloping")],
    )
    ca = FloatField(label="CA", validators=[InputRequired()])
    thal = IntegerField(label="Thal", validators=[InputRequired()])

    check = SubmitField(label="Check")
