from flask import { 
                    Flask, 
                    render_template,
                    url_for,
                    redirect
                    }
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = { 
    'db': 'users' 
}
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
db = MongoEngine(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('components/login/login.html')


if __name__ == '__main__':
    app.run(port=9000, debug=True)
