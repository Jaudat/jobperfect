__author__ = 'cevdet'

import datetime
from config import db


class Profile(db.Document):
    username = db.StringField(required=False, unique=False, max_length=50) # this is not used and will be deprecated if possible
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    created_on = db.DateTimeField(default=datetime.datetime.now, required=True)
    modified_on = db.DateTimeField(default=datetime.datetime.now, required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    #display_pic = ...

    job_histories = db.ListField(db.EmbeddedDocumentField(JobHistory))
    past_projects = db.ListField(db.EmbeddedDocumentField(PastProject))
    skillcases = db.ListField(db.EmbeddedDocumentField(Skillcase))


class JobHistory(db.EmbeddedDocuments): # Experience or Employment History
    stime = db.DateTimeField()
    ftime = db.DateTimeField()
    title = db.StringField()
    company = db.StringField()
    city = db.Stringfield()
    prov = db.Stringfield()
    country = db.Stringfield()

class PastProject(db.EmbeddedDocuments):
    name = db.Stringfield()
    paragraph = db.TextField()
    link = db.URLField()
    quote = db.ListField(db.TextField()) # List containing person whe qoted and
                                         # quote that validates what is being said

class Skillcase(db.EmbeddedDocuments): # Skills and Expertise
    skill = db.StringField()
    descriptions = db.Listfield(db.TextField())

#####################################################################################
#           TODO Add rest Afterwords to Profile
#####################################################################################

class FormalEdu(db.EmbeddedDocument):
    pass

class RelevantCourse(db.EmbeddedDocuments):
    pass

class EventAttendance(db.EmbeddedDocuments): # Conferences etc.
    pass

class JoinedAssociation(db.EmbeddedDocuments):
    pass

class PeerRecommendation(db.EmbeddedDocuments):
    pass

# TODO Add Account Settings into Profile database
    # this may include the first and last name, email address etc.
    # it will also include min pay ready to accept(if any), (or GPA)?
    # or if willing to relocate or even what type of job looking for e.g Intern/Full-time etc
    # could also have career progression settings what job you want for your next part of career



#####################################################################################
#          TODO Employer Database
#####################################################################################