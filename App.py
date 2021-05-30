from flask import Flask, config, render_template, request, url_for, redirect, flash
from flask.wrappers import Request

app = Flask(__name__)

@app.route('/')
def Load():
    return render_template('load.html')

@app.route('/index')
def Index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000 ,debug=True)