from Project2_Flask import app, forms, main_functions
from flask import request, render_template
import requests

"""
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
"""

@app.route('/')
def WelcomeScreen():

    my_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")
    my_key= my_key_dict["NYT_API_Project2_Key"]

    #URL for books
    url_books_base="https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key="
    url_books=url_books_base+my_key

    #URL for movies
    url_movies_base="https://api.nytimes.com/svc/movies/v2/reviews/picks.json?api-key="
    url_movies=url_movies_base+my_key

    main_functions.save_to_file(requests.get(url_books).json(), "JSON_Files/tmp_results.json")