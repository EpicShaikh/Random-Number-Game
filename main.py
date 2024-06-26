import pyinputplus as pyip
from replit import db
import os
import random
import time
import datetime
from flask import Flask, request, redirect

app = Flask(__name__, static_url_path='/static')

f = open("static/num.txt", "r")
login_atts = eval(f.read())
f.close()

@app.route('/')
def home():
  page = ""
  f = open("pages/home.html", "r")
  page = f.read()
  f.close()
  return page
  
@app.route('/rng-menu')
def menu():
  page = ""
  f = open("pages/rng-menu.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/login')
def login():
  page = ""
  f = open("pages/login.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/signup')
def signup():
  page = ""
  f = open("pages/signup.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/signed-up', methods=["POST"])
def signed():
  form = request.form
  user = form["username"]
  
  if db.keys() == set():
    return redirect("/rng-menu")
    

  elif user in db["users"].keys():
    page = """<!DOCTYPEhtml>
<html>
  <head>
    <title>
      Sign Up Unsuccessful
    </title>
    <link rel="icon" href="/static/favicon.ico">
    <link href="static/CSS/style.css" rel="stylesheet" type="text/css">
  </head>

  <body>
    <h1>
      Username already taken.
    </p>
    <button type='button' onclick='location.href="/signup"'>
      Try Again
    </button>
  </body>
</html>"""
    return page

  else:
    return redirect("/rng-menu")

@app.route('/login-success', methods=["POST"])
def login_success():
  page = ""
  form = request.form
  user = form["username"]
  if db.keys() == set():
    page = """<!DOCTYPEhtml>
    <html>
    <head>
    <title>Login Unsuccessful</title>
    <link rel="icon" href="/static/favicon.ico">
    <link href="static/CSS/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
    <h1>Login Unsuccessful</h1>
    <p>No accounts have been created for you to log into.</p>
    <button type='button' onclick="location.href='/login'">You can try again here</button>
    </body>
    </html>"""
    return page

  elif user not in db["users"].keys():
    page = """<!DOCTYPEhtml>
    <html>
    <head>
    <title>Login Unsuccessful</title>
    <link rel='icon' href='/static/favicon.ico'>
    <link href='static/CSS/style.css' rel='stylesheet' type='text/css'>
    </head>
    <body>
    <h1>Login Unsuccessful</h1>
    <p>Username not found.</p>
    <button type='button' onclick="location.href='/login'">You can try again here</button>
    </body>
    </html>"""
    return page

  elif user in db["users"].keys():
    page = """<!DOCTYPEhtml>
    <html>
    <head>
    <title>Login Successful</title>
    <link rel="icon" href="/static/favicon.ico">
    <link href='static/CSS/style.css' rel='stylesheet' type='text/css'>
    </head>
    <body>
    <h1>Login Successful</h1>
    <p>Welcome, {user}!</p>
    <button type='button' onclick="location.href='/play' class='play'">Play</button>
    </body>
    </html>"""
    page = page.replace("{user}", user)
    f = open("static/num.txt", "w")
    f.write(str(login_atts))
    f.close()
    return page
        
  else:
    return redirect("/rng-menu")

@app.route('/loginfail')
def loginfail():
  page = """<!DOCTYPEhtml>
  <html>
  <head>
  <title>Login Unsuccessful</title>
  <link rel='icon' href='/static/favicon.ico'>
  <link href='static/CSS/style.css' rel='stylesheet' type='text/css'>
  </head>
  <body>
  <h1>Login Unsuccessful</h1>
  <button type='button' onclick="location.href='/login'">You can try again here</button>
  </body>
  </html>"""
  return page

num = random.randint(1, 100)
@app.route('/play/<variable>', methods=["POST", "GET"])
def play(variable):
  page = ""
  f = open("pages/play.html", "r")
  page = f.read()
  f.close()

  if request.method == "GET":
    form = request.form
    guess = int(form["guess"])

  elif request.method == "POST":
    form = request.form
    
  
  return page

app.run(host='0.0.0.0', port=81)