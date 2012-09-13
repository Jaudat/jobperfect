__author__ = 'cevdet'

from flask import Blueprint, request, render_template, session, redirect, url_for, current_app
from model import Profile, JobHistory, PastProject, Skillcase
from flask.ext.mongoengine import DoesNotExist, MultipleObjectsReturned, ValidationError
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
                # TODO pquote is not here, need to implement....
                sgroup = request.form["skill_name"]
                sbullet = request.form["skill_bps"]

                result.first_name = fname
                result.last_name = lname
                result.save()
                result.job_histories
                if stime and etime:
                    try:
                        jh = JobHistory(stime=strptime(stime, "%B %Y"),ftime=strptime(etime, "%B %Y"),
                        title=title, company=cname, city=ccity, prov=cprov, country=cnation)
                    except ValidationError:
                        return "render the template and stime or ftime is wrong format"
                else:
                    jh = JobHistory(title=title, company=cname, city=ccity, prov=cprov, country=cnation)
                result.job_histories.append(jh)
                result.save()
                result.past_projects
                if plink:
                    try:
                        pj = PastProject(name=pname, paragraph=pdescription, link=plink)
                    except ValidationError:
                        return "render template and link is wrong format"
                else:
                    pj = PastProject(name=pname, paragraph=pdescription)
                result.past_projects.append(pj)
                result.save()
                sk = Skillcase(skill=sgroup,descriptions=sbullet)
                result.skillcases.append(sk)
                result.save()
                return redirect(url_for('.showPost'))
            else:
                current_app.logger.debug("Method is GET")
                return render_template('editProfiles.html', results=result)
    else: return "You are not logged in"

            # List of jinja2 variables in editProfiles.html
            #  frstNme="", lstNme="", frst_yr="", end_yr=""
            #, job_tl="", work_name="", work_city="", work_prov="", work_nation="", proj_name="", proj_para=""
            #, proj_link="", skill_name="", skill_bps="")

@userP.route('/myProfile', methods=['GET', 'POST'])
def showPost():
    return "Profile Shown"


