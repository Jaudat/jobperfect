__author__ = 'cevdet'

import datetime
from config import db
from flask_mongoengine import *


class Profile(db.Document):
    vanity = db.StringField(required=False, unique=False, max_length=50) # this is not used and will be deprecated if possible
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    created_on = db.DateTimeField(default=datetime.datetime.now, required=True)
    modified_on = db.DateTimeField(default=datetime.datetime.now, required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    #display_pic = ...

    job_histories = db.ListField(db.EmbeddedDocumentField('JobHistory'))
    past_projects = db.ListField(db.EmbeddedDocumentField('PastProject'))
    skillcases = db.ListField(db.EmbeddedDocumentField('Skillcase'))


class JobHistory(db.EmbeddedDocument): # Experience or Employment History
    stime = db.DateTimeField()
    ftime = db.DateTimeField()
    title = db.StringField()
    company = db.StringField()
    city = db.StringField()
    prov = db.StringField()
    country = db.StringField()

class PastProject(db.EmbeddedDocument):
    name = db.StringField()
    paragraph = db.StringField()
    link = db.URLField()
    quote = db.StringField()            # List containing person whe qoted and
                                         # quote that validates what is being said

class Skillcase(db.EmbeddedDocument): # Skills and Expertise
    skill = db.StringField()
    descriptions = db.StringField()

#####################################################################################
#           TODO Add rest Afterwords to Profile
#####################################################################################

class FormalEdu(db.EmbeddedDocument):
    pass

class RelevantCourse(db.EmbeddedDocument):
    pass

class EventAttendance(db.EmbeddedDocument): # Conferences etc.
    pass

class JoinedAssociation(db.EmbeddedDocument):
    pass

class PeerRecommendation(db.EmbeddedDocument):
    pass

# TODO Add Account Settings into Profile database
    # this may include the first and last name, email address etc.
    # it will also include min pay ready to accept(if any), (or GPA)?
    # or if willing to relocate or even what type of job looking for e.g Intern/Full-time etc
    # could also have career progression settings what job you want for your next part of career



#####################################################################################
#          TODO Employer Database
#####################################################################################