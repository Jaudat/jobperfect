__author__ = 'cevdet'

import datetime
from config import db
from flask import current_app


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

    def getJH(self, name, comp): #TODO Use the start and finish years to get the precise JH
        for jh in self.job_histories:
            if jh.title == name and jh.company == comp:
                return jh
        else: return None

    def setJH(self, object, name, comp):
        i=0
        while i < len(self.job_histories):   #TODO Use the start and finish years to get the precise JH
            current_app.logger.debug(" i is %i and title is %s" % (i, self.job_histories[i].title))
            if self.job_histories[i].title == name and self.job_histories[i].company == comp:
                current_app.logger.debug("Entered if Statement")
                self.job_histories[i] = object
                current_app.logger.debug("%s" % self.job_histories[i].title)
                self.save()
                return self.job_histories
            i+=1

    def getPP(self, name, para): #TODO Use the start and finish years to get the precise JH
         for pp in self.past_projects:
             if pp.name == name and pp.paragraph == para:
                 return pp
         else: return None

    def setPP(self, object, name, para):
        i=0
        while i < len(self.past_projects):   #TODO Use the start and finish years to get the precise JH
            current_app.logger.debug(" i is %i and title is %s" % (i, self.past_projects[i].name))
            if self.past_projects[i].name == name and self.past_projects[i].paragraph == para:
                current_app.logger.debug("Entered if Statement")
                self.past_projects[i] = object
                current_app.logger.debug("%s" % self.past_projects[i].name)
                self.save()
                return self.past_projects
            i+=1

    def getSE(self, name, para): #TODO Use the start and finish years to get the precise JH
         for se in self.skillcases:
             if se.skill == name and se.descriptions == para:
                 return se
         else: return None

    def setSE(self, object, name, para):
        i=0
        while i < len(self.skillcases):   #TODO Use the start and finish years to get the precise JH
            current_app.logger.debug(" i is %i and title is %s" % (i, self.past_projects[i].name))
            if self.skillcases[i].skill == name and self.skillcases[i].descriptions == para:
                current_app.logger.debug("Entered if Statement")
                self.skillcases[i] = object
                current_app.logger.debug("%s" % self.past_projects[i].name)
                self.save()
                return self.skillcases
            i+=1

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