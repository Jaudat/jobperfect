__author__ = 'cevdet'

from flask import Blueprint, request, render_template, session, redirect, url_for
from model import Profile, JobHistory, PastProject, Skillcase
from flask.ext.mongoengine import DoesNotExist, MultipleObjectsReturned
from time import strftime, strptime


userP = Blueprint('userProfiles', __name__,
                        template_folder='templates')


@userP.route('/newjh/', methods=['GET', 'POST'])
def newJH():
    if 'email' in session:
           emailz = session['email']
           try:
               result = Profile.objects.get(email=emailz)
           except DoesNotExist:
               return "You are not logged in"
           else:
               if request.method == 'POST':
                   stime = request.form["start_yr"]
                   etime = request.form["end_yr"]
                   title = request.form["emp_tle"]
                   cname = request.form["comp_name"]
                   ccity = request.form["comp_city"]
                   cprov = request.form["comp_prov"]
                   cnation = request.form["comp_nation"]
                   result.job_histories
                   if stime and etime:
                       jh = JobHistory(stime=strptime(stime, "%B %Y"),ftime=strptime(etime, "%B %Y"),
                       title=title, company=cname, city=ccity, prov=cprov, country=cnation)
                   else:
                       jh = JobHistory(title=title, company=cname, city=ccity, prov=cprov, country=cnation)
                   result.job_histories.append(jh)
                   result.save()
                   return redirect(url_for('.showProfile'))
               else:
                   return render_template('newJHs.html', results=result)
    else: return "You are not logged in"

@userP.route('/newpp/', methods=['GET', 'POST'])
def newPP():
    if 'email' in session:
        emailz = session['email']
        try:
            result = Profile.objects.get(email=emailz)
        except DoesNotExist:
            return "You are not logged in"
        else:
            if request.method == 'POST':
                pname = request.form["proj_name"]
                pdescription = request.form["proj_para"]
                plink = request.form["proj_link"]
                # TODO pquote is not here, need to implement....
                result.past_projects
                if plink and plink != "None":
                    pj = PastProject(name=pname, paragraph=pdescription, link=plink)
                else:
                    pj = PastProject(name=pname, paragraph=pdescription)
                result.past_projects.append(pj)
                result.save()
                return redirect(url_for('.editProfile'))
            else:
                return render_template('newPPs.html', results=result)
    else: return "You are not logged in"


@userP.route('/newse/', methods=['GET', 'POST'])
def newSE():
    if 'email' in session:
        emailz = session['email']
        try:
            result = Profile.objects.get(email=emailz)
        except DoesNotExist:
            return "You are not logged in"
        else:
            if request.method == 'POST':
                sgroup = request.form["skill_name"]
                sbullet = request.form["skill_bps"]
                sk = Skillcase(skill=sgroup,descriptions=sbullet)
                result.skillcases.append(sk)
                result.save()
                return redirect(url_for('.editProfile'))
            else:
                return render_template('newSEs.html', results=result)
    else: return "You are not logged in"


@userP.route('/MyAccount/', methods=['GET', 'POST'])
def newEntry(): #TODO Change this to account settings and finish
    if 'email' in session:
        emailz = session['email']
        try:
            result = Profile.objects.get(email=emailz)
        except DoesNotExist:
            return "You are not logged in"
        else:
            if request.method == 'POST':
                fname = request.form["fname"]
                lname = request.form["lname"]
                vname = request.form["vname"]
                result.first_name = fname
                result.last_name = lname
                result.vanity = vname #TODO need a place to change Vanity URL if unique
                result.save()
                return redirect(url_for('.showProfile', vanity=result.vanity))
            else:
                return render_template('newEntry.html', results=result)
    else: return "You are not logged in"


@userP.route('/myProfile/<vanity>/', methods=['GET'])
def showProfile(vanity):
    try:
        result = Profile.objects.get(vanity=vanity)
    except (DoesNotExist, MultipleObjectsReturned):
        return "Wrong URL"
    else:
        if 'email' in session:
            emailz = session['email']
            if result.email == emailz:
                    return render_template('showProfiles.html', results=result)
            else: return "You are not logged in"
        else: return render_template('anonProfiles.html', results=result)


@userP.route('/______auto-build_______/', methods=['GET'])
def autoBuildProfileURL():
    emailz = session['email']
    try:
        result = Profile.objects.get(email = emailz)
    except (DoesNotExist, MultipleObjectsReturned):
        return "You are Not Logged In"
    else: return redirect('/myProfile/%s' % result.vanity)




@userP.route('/edit/', methods=['GET', 'POST'])
def editProfile():
    if 'email' in session:
        emailz = session['email']
        try:
            result = Profile.objects.get(email=emailz)
        except DoesNotExist:
            return "You are not logged in"
        else:
            return render_template('editProfiles.html', results=result, vanityz=result.vanity)
    else: return "You are not logged in"


@userP.route('/editjh/', methods=['GET', 'POST'])
def editJH():
    if 'email' in session:
       emailz = session['email']
       try:
           result = Profile.objects.get(email=emailz)
       except DoesNotExist:
           return "You are not logged in"
       else:
           title = request.args['title']
           company = request.args['company']
           if request.method == 'GET':
               jhDict = result.getJH(title, company)
               return render_template("editJHs.html", jh=jhDict)
           else:
               stime = request.form["start_yr"]
               etime = request.form["end_yr"]
               ctitle = request.form["emp_tle"]
               cname = request.form["comp_name"]
               ccity = request.form["comp_city"]
               cprov = request.form["comp_prov"]
               cnation = request.form["comp_nation"]
               if stime and etime:
                   jh = JobHistory(stime=strptime(stime, "%B %Y"),ftime=strptime(etime, "%B %Y"),
                   title=ctitle, company=cname, city=ccity, prov=cprov, country=cnation)
               else:
                   jh = JobHistory(title=ctitle, company=cname, city=ccity, prov=cprov, country=cnation)
               result.setJH(jh, title, company)
               return redirect(url_for('.editProfile'))
    else: return "You are not logged in"


@userP.route('/editpp/', methods=['GET', 'POST'])
def editPP():
    if 'email' in session:
       emailz = session['email']
       try:
           result = Profile.objects.get(email=emailz)
       except DoesNotExist:
           return "You are not logged in"
       else:
           title = request.args['title']
           para = request.args['para']
           if request.method == 'GET':
               ppDict = result.getPP(title, para)
               return render_template("editPPs.html", pp=ppDict)
           else:
               pname = request.form["proj_name"]
               pdescription = request.form["proj_para"]
               plink = request.form["proj_link"]
               # TODO pquote is not here, need to implement....
               if plink and plink != "None": pj = PastProject(name=pname, paragraph=pdescription, link=plink)
               else:pj = PastProject(name=pname, paragraph=pdescription)
               result.setPP(pj, title, para)
               return redirect(url_for('.editProfile'))
    else: return "You are not logged in"


@userP.route('/editse/', methods=['GET', 'POST'])
def editSE():
    if 'email' in session:
       emailz = session['email']
       try:
           result = Profile.objects.get(email=emailz)
       except DoesNotExist:
           return "You are not logged in"
       else:
           title = request.args['skill']
           para = request.args['para']
           if request.method == 'GET':
               seDict = result.getSE(title, para)
               return render_template("editSEs.html", se=seDict)
           else:
               sgroup = request.form["skill_name"]
               sbullet = request.form["skill_bps"]
               sk = Skillcase(skill=sgroup,descriptions=sbullet)
               result.setSE(sk, title, para)
               return redirect(url_for('.editProfile'))
    else: return "You are not logged in"

