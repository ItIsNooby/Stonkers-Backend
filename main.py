import threading
from flask import render_template, Flask, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'temporary-secret-key'  # Replace with your own secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with your SQLite database location

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return 'Registration successful!'

@app.route('/login', methods=['POST'])
def login():
    username_email = request.form['username_email']

    user = User.query.filter_by(username=username_email).first()
    if not user:
        user = User.query.filter_by(email=username_email).first()

    if user:
        return 'Login successful!'
    else:
        return 'Invalid credentials!'

@app.route('/table/')
def table():
    return render_template("table.html")

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8080")
