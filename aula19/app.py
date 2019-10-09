from flask import Flask, escape, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/presentes/")
def presentes():
    return "Hoje estão aqui: Helena, João e o Julio"

@app.route('/user/<username>')
def show_user_profile(username):
    username += " da Silva"
    return 'O Usuário é o(a): %s' % escape(username)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/me")
def me_api():
    return {
        "username": 'user.username',
        "theme": 'user.theme',
        "image": 'url_for("user_image", filename=user.image)',
    }
