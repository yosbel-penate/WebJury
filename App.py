from flask import Flask, config, render_template, request, url_for, redirect, flash,jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config["MONGODB_HOST"] = "mongodb+srv://mongouser:My6Gmkc3Zno7SVQ7@cluster0.kfbtu.mongodb.net/Personal?retryWrites=true&w=majority"

db = MongoEngine(app)

class User(db.DynamicDocument):
    pass

@app.route('/create')
def create():
    users = User.objects()
    return jsonify(users), 10

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