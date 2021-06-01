from flask import Flask, config, render_template, request, url_for, redirect, flash

app = Flask(__name__)

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