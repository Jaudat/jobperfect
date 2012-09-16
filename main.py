__author__ = 'cevdet'


from config import app
from userAccounts import userA
from userProfiles import userP


app.register_blueprint(userA)
app.register_blueprint(userP)

#@app.route('/random/')
#def random():
#    pass
#
#with app.test_request_context():
#    print url_for('random', next='hello', power='major')

if __name__ == '__main__':
    app.run()




