#!/usr/bin/python3
"""starts the pathway web application"""
from models import storage
from models.user import User
from models.parcel import Parcel
from models.review import Review
from os import environ
from flask import Flask, render_template, url_for, flash, redirect
from web_flask.forms import RegistrationForm, LoginForm, SearchForm, ParcelForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, AnonymousUserMixin



app = Flask(__name__)

app.config['SECRET_KEY'] = '9abf69b1cf421af6441aeefd80ce0081'
bcrypt = Bcrypt()
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
        return storage.get(User, user_id)



@app.teardown_appcontext
def close_db(error):
    """Remove the current sqlalchemy session"""
    storage.close()


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    """pathway web app"""
    parcels = storage.all(Parcel).values()
    users = storage.all(User).values()
    parcels_sorted = sorted(parcels, key=lambda parcel: parcel.created_at, reverse=True)
    return render_template('home.html', parcels=parcels_sorted, users=users)


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    '''registration'''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = form.password.data
        '''bcrypt.generate_password_hash(form.password.data).decode('utf-8')'''
        user = User(username=form.username.data,
                    phone_number=form.phone_number.data, email=form.email.data, password=hashed_password)
        storage.new(user)
        storage.save()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    '''logging in'''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.is_available(User, "email", form.email.data)
        if user and (user.password == form.password.data):
            '''if user:'''
            print("Stored Password Hash:", user.password)
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Failed!, check email and/or password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/post', methods=['GET', 'POST'], strict_slashes=False)
def post_parcel():
    '''post parcel'''
    try:
        form = ParcelForm()
        if form.validate_on_submit():
            parcel = Parcel(sender_id=current_user.id,
                            origin=form.origin.data,
                            destination=form.destination.data,
                            size_l_cm=form.size_l_cm.data,
                            size_w_cm=form.size_w_cm.data,
                            size_h_cm=form.size_h_cm.data,
                            weight_kg=form.weight_kg.data,
                            offered_amount=form.offered_amount.data)
            storage.new(parcel)
            storage.save()
            flash(f'Parcel posted', 'success')
            return redirect(url_for('home'))
        return render_template('post_parcel.html', title='Post Parcel', form=form)
    except AttributeError as e:
        if isinstance(current_user, AnonymousUserMixin):
            return redirect(url_for('register'))
        else:
            raise e


@app.route('/search', methods=['POST'], strict_slashes=False)
def search():
    '''process search'''
    parcels = storage.all(Parcel).values()
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    found = []
    for parcel in parcels:
        if (parcel.origin.lower() == origin.lower()) or (parcel.destination.lower() == destination.lower()):
            found.append(parcel)
        found_sorted = sorted(found, key=lambda found: found.created_at, reverse=True)
        return render_template("search.html", found=found_sorted)
    return render_template("home.html")



@app.route('/landingpage', strict_slashes=False)
def landing():
    '''landing page'''
    return render_template('landingpage.html', title='Welcome to PP')


@app.route('/logout')
def logout():
    '''log out'''
    logout_user()
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
