from Project2_Flask import app
from flask import request, render_template

@app.route('/')
def helloWeb():
    fname = "Ed"
    lname = "Car"
    return "Hello {0} {1}, the app is working.".format(fname, lname)