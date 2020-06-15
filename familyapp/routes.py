from Familyapp.familyapp import app,db,mail
from flask import render_template,url_for,redirect,request,flash
from Familyapp.familyapp.forms import LoginForm,RegisterForm
from Familyapp.familyapp.models import Users
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,current_user,login_required
from flask_mail import Message
import secrets,os

@app.route("/",methods=['GET','POST'])
def getaccess():
    return render_template('getaccess.html')

@app.route("/family_tree",methods=['GET','POSt'])
def familytree():
    return render_template('familytree.html')

@app.route('/login/<name>',methods=['POST','GET'])
def login(name):
    form=LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.passwd,form.password.data):
                login_user(user)
                flash('Login Successful','success')
                return redirect(url_for('getaccess'))
            else:
                flash('password incorrect','danger')
                return redirect(url_for('login',name=name))
        else:
            flash('username incorrect','danger')
            return redirect(url_for('login', name=name))
    else:
        return render_template('login.html',form=form,name=name)


def save_picture(form_picture):
    random_hash = secrets.token_hex(8)
    _, ext = os.path.splitext(form_picture.filename)
    image_fn = random_hash+ext
    image_path = os.path.join(app.root_path, 'static/profile_pics/', image_fn)
    form_picture.save(image_path)
    return image_fn


@app.route('/register',methods=['POST','GET'])
@login_required
def register():
    if current_user.is_admin:
        form=RegisterForm()
        if form.validate_on_submit():
            hashed_password=generate_password_hash(form.password.data, method='sha256')
            new_user=Users(name=form.name.data,email=form.email.data,passwd=hashed_password)
            if form.image.data:
                image_file=save_picture(form.image.data)
                new_user.image=image_file
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('getaccess'))
        else:
            return render_template('register.html',form=form)
    else:
        flash('Only Pranav Sinha can access this page','danger')
        return redirect(url_for('login',name='Pranav Sinha'))


