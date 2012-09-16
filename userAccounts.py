__author__ = 'cevdet'

from flask import Blueprint, render_template, request, redirect, url_for, session, flash, escape
from flask.ext.bcrypt import generate_password_hash,check_password_hash
from flask.ext.mongoengine import ValidationError, DoesNotExist, MultipleObjectsReturned
from model import Profile



userA = Blueprint('userAccounts', __name__,
                        template_folder='templates')

@userA.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        emailz = request.form['email']
        pazz = request.form['password']
        veri = request.form['verify']
        # If password and verify fields match then create new BSON Document
        if len(pazz) > 6:
            if pazz == veri:
                pazz = generate_password_hash(pazz)
                new = Profile(email=emailz, password=pazz, vanity=emailz)
                #checks if email address is not in use
                try:
                    Profile.objects.get(email=emailz)
                # If the email address isn't taken
                except DoesNotExist:
                    #Checks if email address is the right format
                    try:
                        new.save()
                    # if email address not in right format
                    except (ValidationError, MultipleObjectsReturned):
                        return render_template('signup.html', eerror="Email is of incorrect format", verror="", perror="")
                    else:
                        session['email'] = emailz
                        flash('You were logged in')
                        return redirect('/MyAccount/')
                else: return render_template('signup.html', verror="", eerror="Email Address is already Taken", perror="")
            else: return render_template('signup.html', verror="Passwords do not match", eerror="", perror="", em=emailz)
        else: return render_template('signup.html', verror="", eerror="", perror="Password has to be at least 6 characters long", em=emailz)
    else: return render_template('signup.html', verror="",perror="",eerror="")

@userA.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emailz = request.form["html_email"]
        pazz = request.form["html_password"]
        try:
            p = Profile.objects.get(email=emailz)
        except ValidationError:
                    return render_template("login.html", invalid="Email is of wrong format")
        except (DoesNotExist, MultipleObjectsReturned):
            return render_template("login.html", invalid="Email is not registered with us")
        else:
            if check_password_hash(p.password, pazz):
                session['email'] = emailz
                flash('You were logged in')
                return redirect('/myProfile/%s' % p.vanity)
            else: render_template("login.html", invalid="Wrong Password")
    return render_template("login.html", invalid="")


@userA.route('/logout/')
def logout():
    session.pop('email', None)
    return "You are logged out"
