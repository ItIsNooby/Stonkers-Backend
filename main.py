import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.players import initPlayers

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.player import player_api


# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

app = Flask(__name__)
app.config['SECRET_KEY'] = 'temporary-secret-key'  # Replace with your own secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with your SQLite database location

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

admin = Admin(app)

class UserView(ModelView):
    column_list = ['username', 'email']  # Columns to display in the user list

admin.add_view(UserView(User, db.session))

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return 'Registration successful!'


@app.route('/login', methods=['POST'])
def login():
    username_email = request.form['username_email']
    password = request.form['password']

    user = User.query.filter_by(username=username_email).first()
    if not user:
        user = User.query.filter_by(email=username_email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        return 'Login successful!'
    else:
        return 'Invalid credentials!'


# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404



@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")



# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8086")
