__author__ = 'cevdet'


from config import app
from userAccounts import userA
from userProfiles import userP



app.register_blueprint(userA)
app.register_blueprint(userP)
#python main.py

if __name__ == '__main__':
    app.run()




