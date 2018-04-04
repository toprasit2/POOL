from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return 'You are logged in as' + session['username']

    return render_template('components/login/login.html')


@app.route('/myproject')
def home():
    return render_template('components/my-project/content.html')


@app.route('/community')
def community():
    return render_template('components/community/content.html')


@app.route('/processor')
def processor():
    return render_template('components/processor/content.html')


@app.route('/view')
def view():
    return render_template('components/view/content.html')


@app.route('/register')
def register():
    return render_template('page/register/register.html')


if __name__ == '__main__':
    app.run(port=9000, debug=True)
