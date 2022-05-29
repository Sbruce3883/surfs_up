from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

from flask import Flask
app = Flask(__name__)
@app.route('/')
def smart_girl():
    return 'I am a smart girl'