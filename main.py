from flask import Flask, request, redirect, render_template
from helpers import valid_credentials, valid_email
import string


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    error = request.args.get("error")
    return render_template("signup_form.html", error=error) 

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email'] 
    
    if username =="":
       error = "The username is required"
       return render_template("signup_form.html", error=error, username=username, email=email)
    if not valid_credentials(username):
       error = "The username is not valid"
       return render_template("signup_form.html", error=error, username="", email=email)
    if password =="":
       error = "The password is required"
       return render_template("signup_form.html", error=error, username=username, email=email)
    if not valid_credentials(password):
       error = "The password is not valid"
       return render_template("signup_form.html", error=error, username=username, email=email)
    if verify_password =="":
       error = "This fild is required"
       return render_template("signup_form.html", error=error, username=username, email=email)
    if password != verify_password:
       error = "The password does not match"
       return render_template("signup_form.html", error=error, username=username, email=email)
    if email != "" and not valid_email(email):
       error = "The email is not valid"
       return render_template("signup_form.html", error=error, username=username, email="") 
           
 
    return render_template("welcome.html", username=username)


app.run()