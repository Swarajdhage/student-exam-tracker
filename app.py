from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os

from forms import RegistrationForm, LoginForm, ExamForm
from models import db, User, Exam

# --- App Config ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Uploads
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)

with app.app_context():
    db.create_all()

# --- Routes ---
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            username=form.username.data,
            password=hashed_pw,
            phone=form.phone.data,
            gender=form.gender.data,
            dob=form.dob.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        flash("Please log in first", "warning")
        return redirect(url_for('login'))

    form = ExamForm()
    exams = Exam.query.order_by(Exam.date.asc()).all()

    if form.validate_on_submit():
        if request.form.get('exam_id'):  # Edit mode
            exam = Exam.query.get(int(request.form.get('exam_id')))
        else:  # New record
            exam = Exam()

        exam.name = form.name.data
        exam.date = form.date.data

        # Handle file uploads
        if form.application_file.data:
            filename = secure_filename(form.application_file.data.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            form.application_file.data.save(filepath)
            exam.application_file = filename

        if form.fee_file.data:
            filename = secure_filename(form.fee_file.data.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            form.fee_file.data.save(filepath)
            exam.fee_file = filename

        db.session.add(exam)
        db.session.commit()

        flash("Exam saved successfully!", "success")
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', username=session['username'], form=form, exams=exams)

@app.route('/edit_exam/<int:id>')
def edit_exam(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    exam = Exam.query.get_or_404(id)
    form = ExamForm(obj=exam)
    exams = Exam.query.order_by(Exam.date.asc()).all()
    return render_template('dashboard.html', username=session['username'], form=form, exams=exams, edit_id=exam.id)

@app.route('/toggle_exam/<int:id>', methods=['POST'])
def toggle_exam(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    exam = Exam.query.get_or_404(id)
    exam.is_completed = not exam.is_completed
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out", "info")
    return redirect(url_for('login'))

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
