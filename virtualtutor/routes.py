"""
Routes for the Virtual Tutor application
Handles navigation, assessments, and Bayesian Knowledge Tracing calculations
"""
from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify, flash
from virtualtutor.forms import RegistrationForm, LoginForm
from virtualtutor.models import User
from virtualtutor import db
from model.calc import calculate_knowledge_level

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/home')
def home():
    """Main landing page showing subject selection"""
    return render_template('home.html')


@bp.route('/about')
def about():
    """About page"""
    return render_template('about.html')


# Subject Unit Routes
@bp.route('/unitchem')
def unit_chem():
    """Chemistry units"""
    return render_template('units_chem.html')


@bp.route('/unitphysics')
def unit_physics():
    """Physics units"""
    return render_template('units_physics.html')


@bp.route('/unitmath')
def unit_math():
    """Mathematics units"""
    return render_template('units_math.html')


@bp.route('/unitbio')
def unit_bio():
    """Biology units"""
    return render_template('units_biology.html')


# Options Routes (Study/Practice/Quiz selection)
@bp.route('/optionschem')
def options_chem():
    """Chemistry learning options"""
    return render_template('options_chem.html')


@bp.route('/optionsphysics')
def options_physics():
    """Physics learning options"""
    return render_template('options_physics.html')


@bp.route('/optionsmath')
def options_math():
    """Mathematics learning options"""
    return render_template('options_math.html')


@bp.route('/optionsbio')
def options_bio():
    """Biology learning options"""
    return render_template('options_bio.html')


# Practice Routes
@bp.route('/practice')
def practice():
    """Main practice page"""
    return render_template('practice.html')


@bp.route('/practice1')
def practice1():
    """Practice session 1"""
    return render_template('practice1.html')


@bp.route('/practice2')
def practice2():
    """Practice session 2"""
    return render_template('practice2.html')


@bp.route('/practice3')
def practice3():
    """Practice session 3"""
    return render_template('practice3.html')


@bp.route('/practice4')
def practice4():
    """Practice session 4"""
    return render_template('practice4.html')


@bp.route('/practice5')
def practice5():
    """Practice session 5"""
    return render_template('practice5.html')


@bp.route('/practice_page_chem')
def practice_page_chem():
    """Chemistry practice page"""
    return render_template('practice_page_chem.html')


# Notes Routes
@bp.route('/noteschem')
def notes_chem():
    """Chemistry study notes"""
    return render_template('noteschem.html')


# Assessment Routes
@bp.route('/assessment')
def assessment():
    """Assessment/quiz page"""
    return render_template('assessment.html')


@bp.route('/quiz')
def quiz():
    """Interactive quiz with Bayesian Knowledge Tracing"""
    return render_template('quiz.html')


# Bayesian Knowledge Tracing Calculation
@bp.route('/calc')
def calc():
    """
    Calculate student knowledge level using Bayesian inference
    Takes number of correct answers and returns estimated mastery percentage
    """
    num_correct = request.args.get('num', 0, type=int)

    try:
        # Use Bayesian Knowledge Tracing to estimate knowledge level
        knowledge_level = calculate_knowledge_level(num_correct)
        return jsonify(result=f"{knowledge_level:.2f}")
    except Exception as e:
        return jsonify(result="0.00", error=str(e))


# Authentication Routes
@bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    form = RegistrationForm()
    if form.validate_on_submit():
        # Note: In production, hash passwords using bcrypt
        user = User(username=form.username.data,
                   email=form.email.data,
                   password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    form = LoginForm()
    if form.validate_on_submit():
        # Note: In production, verify hashed passwords
        flash(f'Login successful!', 'success')
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)


@bp.route('/account')
def account():
    """User account page"""
    return render_template('account.html')


@bp.route('/logout')
def logout():
    """User logout"""
    session.clear()
    return redirect(url_for('main.home'))
