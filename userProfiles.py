__author__ = 'cevdet'

from flask import Blueprint, request, render_template, session
from model import Profile


userP = Blueprint('userProfiles', __name__,
                        template_folder='templates')


@userP.route('/editProfile', methods=['GET', 'POST'])
def editProfile():
    if 'email' in session:
        pass
    else: render_template('editProfiles.html')


