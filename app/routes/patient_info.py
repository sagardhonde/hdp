import pickle

from flask import flash, render_template, request
from flask_login.utils import login_required
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
 

from app import app
from app.forms import PatientInfo

ensemble = pickle.load(open("ensemble.pickle", "rb"))


@app.route("/patient_info", methods=["GET", "POST"])
@login_required
def patient_info():
    form = PatientInfo()
    if request.method == "POST":
        data = [
            [
                form.age.data,
                form.gender.data,
                form.chest_pain.data,
                form.resting_bp.data,
                form.sereum_cholestoral.data,
                form.fasting_blood_sugar.data,
                form.resting_ecg.data,
                form.max_heart_rate.data,
                form.exercise_induced_angina.data,
                form.oldpeak.data,
                form.slope.data,
                form.ca.data,
                form.thal.data,
            ]
        ]
        try:
            result = ensemble.predict(data)
            if result[0] == 0:
                flash("The patient doesn't have Heart Disease", "info")
            else:
                flash("The patient has Heart Disease", "info")
        except Exception as e:
            print(e)
            flash("Something went wrong", "danger")
    return render_template("patient_info.html", title="Patient Info - HDP", form=form)
