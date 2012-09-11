__author__ = 'cevdet'

from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_DB"] = "jobperfect"
app.config["SECRET_KEY"] = """|\xb6\xf2\x9b&\xed\xe8\x15\x85\x82N\xfb{\xd3\x16\x97\x98\x9b\x04\x14cc\xb23"""
app.config["DEBUG"] = True

db = MongoEngine(app)







