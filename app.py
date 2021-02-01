from flask import Flask  #, Flask_SQLAlchemy

app = Flask(__name__)
# app.config(['DB_KEY']) = 'put a key here'

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Climb-it Change"