from Familyapp.familyapp import app
from flask import render_template,url_for

@app.route("/",methods=['GET','POST'])
def getaccess():
    return render_template('getaccess.html')

@app.route("/family_tree",methods=['GET','POSt'])
def familytree():
    return render_template('familytree.html')