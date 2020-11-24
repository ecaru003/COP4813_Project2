from Project2_Flask import app, forms
from flask import request, render_template

@app.route('/')
def helloWeb():
    fname = "Ed"
    lname = "Car"
    return "Hello {0} {1}, the app is working.".format(fname, lname)

@app.route('/search', methods=['GET', 'POST'])
def search():
    my_sample_form = forms.SampleForm(request.form)
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        pid = request.form["panther_id"]
        start_date = request.form["start_date"]
        major = request.form["major"]
        campus = request.form["campus"]

        response = [first_name, last_name, pid, start_date, major, campus]
        return render_template('results.html', response=response, major=major, form=my_sample_form)
    return render_template('search.html', form=my_sample_form)