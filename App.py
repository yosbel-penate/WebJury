
from forms import SingupForm, LoginForm
from models import User
from flask import Flask, config, render_template, request, url_for, redirect
from mongoengine import *
from flask_login import LoginManager, current_user, login_user
from werkzeug.urls import url_parse

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
db = connect(host= "mongodb+srv://mongouser:My6Gmkc3Zno7SVQ7@cluster0.kfbtu.mongodb.net/Personal?retryWrites=true&w=majority")

login_manager = LoginManager(app)
login_manager.init_app(app) 

def get_user(email):
    return User.objects(email=email).first()

@login_manager.user_loader
def load_user(user_id):
    return User.objects(user_id).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('Index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SingupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name=name, email=email, password=password)
        user.save()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('Index')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)

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