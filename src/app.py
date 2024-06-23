from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        return render_template('login.html')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
