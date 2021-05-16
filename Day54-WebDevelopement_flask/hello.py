from flask import Flask

app = Flask(__name__)


def bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function
def em(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
@bold
@em
@underlined
def sayBye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)



