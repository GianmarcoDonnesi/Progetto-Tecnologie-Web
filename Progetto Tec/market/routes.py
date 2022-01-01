from market import app
from flask import render_template, session, request, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/inserisci_annuncio')
def inserisci_annuncio():
    return render_template('inserisciannuncio.html')

@app.route('/annunci')
@login_required
def annunci_page():
    items = Item.query.all()
    return render_template('annunci.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f'Account creato! Sei loggato come: {user_to_create.username}', category='success')

        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'Errore durante la creazione di un account: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Sei loggato come: {attempted_user.username}', category='success')
            return redirect(url_for('annunci_page'))
        else:
            flash('Username e password non corrispondono! Riprova', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("Hai effettuato il logout!", category='info')
    return redirect(url_for("home_page"))





