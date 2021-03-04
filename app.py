from flask import render_template, request, redirect, session, jsonify, flash

from wsgi import app

app.secret_key = "administers"


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get("pwd")
        if user == pwd == "admin":
            session['user_info'] = user
            flash('You were successfully logged in')
            return redirect("/index")
        else:
            return render_template("login.html", msg="username or pwd is error")


@app.route("/index", methods=['GET'])
def index():
    user_info = session.get("user_info")
    if not user_info:
        return redirect('/')
    return str(user_info)


@app.route("/logout", methods=['GET'])
def logout():
    del session["user_info"]
    return redirect('/')
