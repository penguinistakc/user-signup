from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/signup", methods=['POST'])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verifyPassword"]
    email = request.form["email"]
    username_error = ''
    password_error = ''
    verify_error = ''
    verify_empty_error = ''
    email_error = ''
    error_condition = False
    
    if len(username) == 0:
        username_error = "That's not a valid username, please re-enter"
        error_condition = True
    

    if len(password) < 3:
        password_error = "Password must have between 3 and 20 characters and no spaces"
        error_condition = True

    elif len(password) > 20:
        password_error = "Password must have between 3 and 20 characters and no spaces"
        error_condition = True

    elif password.count(' ') > 0:
        password_error = "Password must have between 3 and 20 characters and no spaces"
        error_condition = True
    
    if len(verify_password) == 0:
        verify_error = "Verify password field must not be empty"
        error_condition = True

    elif verify_password != password:
        verify_error = "Passwords do not match"
        error_condition = True


    if len(email) > 0:
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must have between 3 and 20 characters"
            error_condition = True
        elif email.count(' ') > 0:
            email_error = "Email must have no spaces"
            error_condition = True
        elif email.count('@') != 1:
            print(email.find('@'))
            email_error = "Email may have only one @"
            error_condition = True
        elif email.count('.') != 1:
            email_error = "Email may have only one period (.)"
            error_condition = True
        
    if error_condition:
        return render_template("signup.html",username_error=username_error,password_error=password_error,username=username,email=email,verify_error=verify_error,email_error=email_error)
    else:
        return redirect(url_for('welcome',username=username))

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html",username=username)

@app.route("/")
def index():
    return render_template("signup.html")

app.run()