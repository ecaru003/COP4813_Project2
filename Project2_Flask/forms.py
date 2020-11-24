from Project2_Flask import app
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, RadioField, SelectField, StringField

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