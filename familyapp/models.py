from familyapp import app,db,login_manager
from flask_login import UserMixin,current_user
from flask_admin.contrib.sqla import ModelView
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_admin import Admin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False, unique=True)
    image=db.Column(db.String(100),nullable=False,default="person.png")
    email=db.Column(db.String(50),nullable=True, unique=True)
    passwd=db.Column(db.String(20), nullable=False)
    is_admin=db.Column(db.Boolean,default=False)

    def get_reset_token(self,expires_sec=1800):
        s=Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(app.config['SECRET_KEY'])
        try:
            user_id=s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)


    def __repr__(self):
        return "User('{}','{}','{}','{}',is_admin='{}')".format(self.id,self.name,self.email,self.image,self.is_admin)

class Numbers(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    number1 = db.Column(db.String(13),nullable=True)
    number2 = db.Column(db.String(13), nullable=True)


    def __repr__(self):
        return "Number('{}','{}','{}','{}')".format(self.id,self.name,self.number1,self.number2)
