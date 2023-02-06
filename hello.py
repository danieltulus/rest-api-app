from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/user/<username>")
def show_user_profile(username):
	return f'Welcome, {escape(username)}'

@app.route('/')
def index():
	return 'Index Page'