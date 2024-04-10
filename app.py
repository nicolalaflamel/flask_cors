from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r'/': {'origins': 'http://127.0.0.1:5000'}})

@app.route("/")
def helloWorld():
    return "Hello, Closed World!"

if __name__ == '__main__':
    app.run(debug=True)
