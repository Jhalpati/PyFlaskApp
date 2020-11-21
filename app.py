from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Introduction to Python"

if __name__ == '__main__':
    app.run()
