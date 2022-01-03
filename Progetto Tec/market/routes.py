from market import app, photos
from flask import render_template, session, request, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, Addproducts
from market import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/annunci')
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
            return redirect(url_for('home_page'))
        else:
            flash('Username e password non corrispondono! Riprova', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("Hai effettuato il logout!", category='info')
    return redirect(url_for("home_page"))

@app.route('/insert_product', methods=['POST', 'GET'])
@login_required
def insert_product():
    form = Addproducts(request.form)

    if request.method == 'POST':
        name = form.nome.data
        price = form.price.data
        cauzione = form.caution.data
        provincia = form.province.data
        description = form.description.data
        image_1 = photos.save(request.files.get('image_1'))
        image_2 = photos.save(request.files.get('image_2'))

        Addpro = Item(name=name, price=price, cauzione=cauzione, provincia=provincia, description=description, image1=image_1, image2=image_2)
        db.session.add(Addpro)
        flash(f'Annuncio Inserito!', category='success')
        db.session.commit()
        return redirect(url_for('annunci_page'))

    return render_template('Inserisci_annuncio.html', title="Inserisci annuncio", form=form)



