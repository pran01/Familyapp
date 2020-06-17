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
    if current_user.is_authenticated:
        return redirect(url_for('home',name=current_user.name))
    return render_template('getaccess.html')


@app.route("/home/<name>",methods=['POST','GET'])
def home(name):
    return render_template('home.html',name=name,Users=Users)

@app.route("/family_tree",methods=['GET','POSt'])
def familytree():
    return render_template('familytree.html',Users=Users)

@app.route('/login/<name>',methods=['POST','GET'])
def login(name):
    form=LoginForm()
    if Users.query.filter_by(name=name).first().email:
        form.email.data=Users.query.filter_by(name=name).first().email
    else:
        form.email.data=name
    if form.validate_on_submit():
        user=Users.query.filter_by(name=name).first()
        if user:
            if check_password_hash(user.passwd,form.password.data):
                login_user(user)
                return redirect(url_for('home',name=name))
            else:
                flash('password incorrect','danger')
                return redirect(url_for('login',name=name))
        else:
            flash('username incorrect','danger')
            return redirect(url_for('login', name=name))
    else:
        return render_template('login.html',form=form,name=name,Users=Users)


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
            new_user=Users(name=form.name.data,passwd=hashed_password)
            if form.image.data:
                image_file=save_picture(form.image.data)
                new_user.image=image_file
            if form.email.data:
                new_user.email=form.email.data
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('getaccess'))
        else:
            return render_template('register.html',form=form)
    else:
        flash('Only Pranav Sinha can access this page','danger')
        return redirect(url_for('login',name='Pranav Sinha'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out Successfully', 'success')
    return redirect(url_for('getaccess'))
