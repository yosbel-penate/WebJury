from flask import Flask, config, render_template, request, url_for, redirect, flash,jsonify, abort
from mongoengine import *
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

connect(host= "mongodb+srv://mongouser:My6Gmkc3Zno7SVQ7@cluster0.kfbtu.mongodb.net/Personal?retryWrites=true&w=majority")
class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.email)
class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Email')
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

users = []
def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)
        flash('Logged in successfully.')
        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)
        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)


@app.route('/create')
def create():
    user = User()
    user.name="pepe2"
    user.email="pepe2@gmail.com"
    user.password="sddjfsfsjflksjfl"
    user.save()
    return jsonify(user.to_json())

@app.route('/read/<id>')
def read(id=0):
    read=User.objects(id).first()
    return jsonify(read.to_json())


@app.route('/')
def Load():
    return render_template('load.html')

@app.route('/index')
def Index():
    return render_template('index.html')

@app.route('/login')
def Login():
    return render_template('login.html')

@app.route('/statement')
def Statement():
    return render_template('statement.html')

if __name__ == '__main__':
    app.run(port=3000 ,debug=True)