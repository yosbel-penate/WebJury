from flask import Flask, config, render_template, request, url_for, redirect, flash,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://mongouser:My6Gmkc3Zno7SVQ7@cluster0.kfbtu.mongodb.net/Personal?retryWrites=true&w=majority"
mongo = PyMongo(app)

db_operations = mongo.db.User

@app.route('/create')
def create():
    new_user ={"user_name":"pepe", "age":"45"}
    db_operations.insert_one(new_user)
    result = {'result' : 'Created successfully'}
    return result

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