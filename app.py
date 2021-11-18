from flask import Flask

# Create a flask instance 
app = Flask(__name__)

# Create Flask routes 
# 1. Define root starting point at highest hierarchy level using "/"
@app.route("/")
def hello_world():
    return "Hello world"