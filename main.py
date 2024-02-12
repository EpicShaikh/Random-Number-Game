import pyinputplus as pyip
from replit import db
import os
import random
import time
from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
  page = ""
  f = open("pages/home.html", "r")
  page = f.read()
  f.close()
  return page
  


app.run(host='0.0.0.0', port=81)