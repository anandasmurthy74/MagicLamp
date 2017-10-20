# Magic Lamp  -   Flask   -  Main.py
from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from flask_pymongo import PyMongo
import bcrypt
from CreateProject import CreateProj

# from flask_admin import Admin
# from flask_mongoengine import MongoEngine
# from flask_admin.contrib.mongoengine import ModelView
# from flask_mongoengine.wtf import model_form
# from flask_admin.model.fields import InlineFormField, InlineFieldList


app = Flask(__name__)


app.config["MONGO_DBNAME"] = "magiclamp"
app.config["MONGO_URI"] = "mongodb://dbuser:Vin75!yaka@ds151153.mlab.com:51153/magiclamp"

mongo = PyMongo(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    # if 'username' in session:
    #     return render_template(url_for('profile/' + session['username']))

    return render_template("index.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw((request.form['pass']).encode('utf-8'), bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return "Users already exists"
    return render_template("register.html")


@app.route("/login", methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username': request.form['username']})
    if login_user:
        if bcrypt.hashpw((request.form['pass']).encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('profile'))

    return 'Invalid Username/password combination'


@app.route("/profile", methods=['GET'])
def profile():
    username = session['username']
    profile = mongo.db.Profile
    profile_data = profile.find_one({'username': username})
    if profile_data is not None:
        return render_template("profile_student.html", mydata=profile_data)
    else:
        return "No user Profile found"


@app.route("/project", methods=['GET'])
def project():
    projId = 1
    prj_Mstr = mongo.db.Profile.find_one({'Projects.projid': projId}, {'Projects': True, '_id': False})
    prjM = prj_Mstr['Projects']
    project_data = mongo.db.Project.find_one({'projId': projId})
    project_data.update(prjM[0])
    if project_data is not None:
        return render_template("project.html", prjdata=project_data)
    else:
        return "No Project found"


@app.route("/createProject", methods=['GET'])
def createProject():
    username = session['username']
    pData = mongo.db.Profile.find_one({'username': username})

    return render_template("CreateProject.html", pdata=pData)


@app.route("/newProj", methods=['POST'])
def newProj():
    nProj = CreateProj()
    nprojId = nProj.addProj(session['username'], request.form['pgrade'], request.form['name'], request.form['description'], request.form['tags'])
    if nprojId > 0:
        pData = mongo.db.Profile.find_one({'username': session['username']}, {'_id': 0})
        if pData:
            return jsonify({'mydata': pData})
    else:
        return jsonify({'error': "no data"})


@app.route("/loadProject", methods=['GET'])
def loadProject():
    # username = session['username']
    prjid = 1  # session['projid']
    profile = mongo.db.Profile.find_one({'username': "anand"})
    prj_list = profile['Projects']
    prj_details = {}
    for x in range(0, len(prj_list)):
        prj = prj_list[x]
        if prjid in prj.values():
            prj_details['pmaster'] = prj
            pcontents = mongo.db.Project.find_one({'projId': prjid})
            prj_details['intro'] = pcontents['introduction']
            prj_details['tockeys'] = pcontents['toc'].keys()
            prj_details['toc'] = pcontents['toc']
            prj_details['img'] = pcontents['images']
            prj_details['toclen'] = len(list(prj_details['tockeys']))
            prj_details['numimgs'] = len(pcontents['images']) - 1
    if prj_details:
        return render_template("loadProject.html", pdata=prj_details)
    else:
        return "Project not found"

# @app.route("/testbootstrap")
# def testbootstrap():
#    return render_template("testbootstrap.html")


if __name__ == "__main__":
    app.secret_key = 'mysecretkey'
    app.run(debug=True)
