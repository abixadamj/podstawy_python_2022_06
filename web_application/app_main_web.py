# https://flask.palletsprojects.com/en/2.1.x/

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<H1>Hello, World!</H1>"


@app.route("/login/<username>")
def hello_2(username):
    return f"<h2>Login - {username} - Inny tekst</h2>"


if __name__ == '__main__':
    app.run(debug=True)
