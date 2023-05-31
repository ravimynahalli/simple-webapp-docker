import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!km ravi"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?im learling devops'

if __name__ == "__main__":
    app.run()
