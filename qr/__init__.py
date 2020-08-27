from flask import Flask 
from flask_pymongo import PyMongo
from flask_qrcode import QRcode

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://rootq:password1@ds023480.mlab.com:23480/attendance?retryWrites=false"
mongo = PyMongo(app)

from qr import routes