from flask import Flask, config, render_template, request, url_for, redirect, flash
from flask.wrappers import Request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'OCwXfA7REx'
app.config['MYSQL_PASSWORD'] = 'yIuQGzEwaF'
app.config['MYSQL_DB'] = 'OCwXfA7REx'
app.config['MYSQL_DATABASE_PORT'] = '3306'
mysql = MySQL(app)

app.secret_key='mysecret_key'

@app.route('/')
def Index():
    cur=cur=mysql.connection.cursor()
    cur.execute('select * from contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts=data)

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('delete from contacts where id={0}'.format(id))
    mysql.connection.commit()
    flash('Row sussefully delete')
    return redirect(url_for('Index'))

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method=='POST':
        fullname=request.form['fullname']
        email=request.form['email']
        phone=request.form['phone']
        cur=mysql.connection.cursor()
        cur.execute("""
        update contacts
        set fullname=%s,
        email=%s,
        phone=%s
        where id=%s
        """, (fullname, email, phone, id))
        mysql.connection.commit()
        flash('Row sussefully update')
        return redirect(url_for('Index'))
        

@app.route('/edit/<id>')
def edit_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('select * from contacts where id={0}'.format(id))
    mysql.connection.commit()
    data = cur.fetchall()
    return render_template('edit-contact.html', contact=data[0])

@app.route('/add_contact', methods=['POST'])
def Add_contact():
    if request.method=='POST':
        fullname=request.form['fullname']
        phone=request.form['phone']
        email=request.form['email']
        print(fullname)
        print(phone)
        print(email)
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES(%s, %s, %s)', (fullname, phone, email))
        flash('Sussefuly save on DB.')
        mysql.connection.commit()
    return redirect(url_for('Index'))
if __name__ == '__main__':
    app.run(port=3000 ,debug=True)