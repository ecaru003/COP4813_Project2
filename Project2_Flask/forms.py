from Project2_Flask import app, main_functions
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, RadioField, SelectField, StringField, BooleanField
import requests

def getList():
    list = [] #list of format "display_name","encoded_name","oldest_date"

    url = "https://api.nytimes.com/svc/books/v3/lists/names.json?api-key="
    api_key = main_functions.read_from_file("Project2_Flask/jsons/api_key.json")["NYT_API_Project2_Key"]
    list_url=url+api_key
    #main_functions.save_to_file(requests.get(list_url).json(),"jsons/bestselling_list.json")
    request_response = requests.get(list_url).json()

    for result in request_response["results"]:
        entry = [result["display_name"], result["list_name_encoded"], result["oldest_published_date"]]
        list.append(entry)

    #print(list)
    return list

def getBooks(list,limit):
    url="https://api.nytimes.com/svc/books/v3/lists/current/"+list+".json?api-key="+main_functions.read_from_file("Project2_Flask/jsons/api_key.json")["NYT_API_Project2_Key"]
    book_list=requests.get(url).json()
    curr_entry = []

    if limit <= 0:
        for entry in book_list["results"]["books"]:
            tup = [entry["book_image"], entry["title"], entry["author"],entry["publisher"],
                   entry["description"], entry["amazon_product_url"], entry["book_review_link"]]
            curr_entry.append(tup)
        return curr_entry

    counter=0
    for entry in book_list["results"]["books"]:
        if counter >= limit:
            break
        tup = [entry["book_image"], entry["title"], entry["author"], entry["publisher"],
               entry["description"], entry["amazon_product_url"], entry["book_review_link"]]
        curr_entry.append(tup)
        counter+=1
    return curr_entry


class SampleForm(FlaskForm):
    fname =      StringField("First Name")
    lname =      StringField("Last Name")
    panther_id = IntegerField("Panther ID")
    start_date = DateField("Start Date", format='%m/%d/%Y')
    major =      RadioField("Major",
                       choices=[('it', 'Information Technology)'),
                                ('cs','Computer Science')])
    campus =     SelectField("Campus",
                       choices=[('mmc', 'Modesto Maidique Campus)'),
                                ('bbc', 'Biscayne Bay Campus'),
                                ('ec', 'Engineering Center')])

class BookListForm(FlaskForm):

    data = getList()

    select_options = []

    for tup in data:
        select_options.append((tup[1],tup[0]))

    chosen_list   = SelectField("NYT Bestselling Lists", choices=select_options)
    chosen_limit  = IntegerField("Entry Limit")
    option_cover  = BooleanField("Cover")


