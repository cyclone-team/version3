from flask import render_template,flash,redirect,request,abort
from app import app
from .forms import LoginForm
from .models import *
from .DBManager import *

db_manager=DBManager("mysql+mysqlconnector","47.107.86.216:3306","root","0C45313cea34","timecontrol")
if db_manager is not None:
    print("DB is OK!")

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': '1' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    db_session = db_manager.create_session()
    form = LoginForm()
    ac=form.account.data
    ps=form.password.data
    #检测表单的填写
    if form.validate_on_submit():
        #if db_session.query(User).filter(ps==User.account) is None:
            #flash('This account is not exist')
            #abort(400)
        #elif ps != db_session.query(User).filter(ac==User.account).first():
            #flash('Password is wrong')
            #abort(401)
        #else:
        flash('Login requested, remember_me=' + str(form.remember_me.data))
            #return redirect("www.baidu.com")
        return render_template('main.html')
    db_session.close()
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])