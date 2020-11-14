from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Intro to Python"

if __name__ == '__main__':
    app.run()
