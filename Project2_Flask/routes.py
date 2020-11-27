from Project2_Flask import app, forms, main_functions
from flask import request, render_template

@app.route('/',      methods=['GET', 'POST'])
@app.route('/books', methods=['GET', 'POST'])
def search():
    bookform = forms.BookListForm(request.form)

    if request.method == "POST":
        list = request.form["chosen_list"]
        limit = request.form["chosen_limit"]
        try:
            limit = int(limit)
        except ValueError:
            limit = -1

        cover   = bookform.option_cover.data
        booklist = forms.getBooks(list, limit)
        response=[list, limit]
        return render_template('results.html', booklist=booklist, cover=cover)


    return render_template('search.html', form=bookform)

