__author__ = 'cevdet'

from flask import Blueprint, request, render_template, session, redirect, url_for, current_app
from model import Profile, JobHistory, PastProject, Skillcase
from flask.ext.mongoengine import DoesNotExist, MultipleObjectsReturned
from time import strftime, strptime


userP = Blueprint('userProfiles', __name__,
                        template_folder='templates')


@userP.route('/editProfile', methods=['GET', 'POST'])
def editProfile():
    current_app.logger.debug("Entering editProfile")
    if 'email' in session:
        current_app.logger.debug("Session is validated")
        emailz = session['email']
        try:
            current_app.logger.debug("Query DB")
            result = Profile.objects.get(email=emailz)
        except DoesNotExist:
            return "You are not logged in"
        else:
            if request.method == 'POST':
                current_app.logger.debug("Method is POST")
                fname = request.form["fname"]
                lname = request.form["lname"]
                stime = request.form["start_yr"]
                etime = request.form["end_yr"]
                title = request.form["emp_tle"]
                cname = request.form["comp_name"]
                ccity = request.form["comp_city"]
                cprov = request.form["comp_prov"]
                cnation = request.form["comp_nation"]
                pname = request.form["proj_name"]
                pdescription = request.form["proj_para"]
                plink = request.form["proj_link"]
                sgroup = request.form["skill_name"]
                sbullet = request.form["skill_bps"]

                query = Profile.objects.get(email=emailz)
                query.first_name = fname
                query.last_name = lname
                query.save()
                #query.job_histories
                #jh = JobHistory(stime=strptime(stime, "%B %Y"),ftime=strptime(etime, "%B %Y"), title=title, company=cname
                #, city=ccity, prov=cprov, country=cnation)
                #query.job_histories.append(jh)
                #query.save()
                #query.past_projects
                #pj = PastProject(name=pname, paragraph=pdescription, link=plink)
                #query.past_projects.append(pj)
                #query.save()
                sk = Skillcase(skill=sgroup,descriptions=sbullet)
                query.skillcases.append(sk)
                query.save()
                return redirect(url_for('.showPost'))
            else:
                current_app.logger.debug("Method is GET")
                hist = result.job_histories[0]
                return render_template('editProfiles.html', job_tl=hist.title, work_name=hist.company)
    else: return "You are not logged in"

            # List of jinja2 variables in editProfiles.html
            #  frstNme="", lstNme="", frst_yr="", end_yr=""
            #, job_tl="", work_name="", work_city="", work_prov="", work_nation="", proj_name="", proj_para=""
            #, proj_link="", skill_name="", skill_bps="")

@userP.route('/myProfile', methods=['GET', 'POST'])
def showPost():
    return "Profile Shown"


