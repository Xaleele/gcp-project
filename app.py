from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello, Simple Flask application' + '\n' 
            + 'This is an additional line' + '\n' 
            + 'This is the third line')