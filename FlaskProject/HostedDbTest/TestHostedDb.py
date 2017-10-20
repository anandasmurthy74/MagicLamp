# Test Hosted db connection

from flask import Flask, render_template, url_for, session, request, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config["MONGODB_URI"] = "mongodb://kay:myRealPassword@mycluster0-shard-00-00-wpeiv.mongodb.net:27017,mycluster0-shard-00-01-wpeiv.mongodb.net:27017,mycluster0-shard-00-02-wpeiv.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin"

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return '<h1> You are logged in as ' + session['username']
    return render_template("index.html")


@app.route('/login')
def login():
    return ''


@app.route('/register')
def register():
    return ''


if __name__ == '__main__':
	app.secret_key = 'mysecretkey'
    app.run(debug=true)
