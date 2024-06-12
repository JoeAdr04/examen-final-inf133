from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id  = db.column(db.integer, primary_key=True)
    name = db.column(db.String(100), unique = True, nullable = False)
    email = db.column(db.String(100), nullable = False)
    password = db.column(db.String(50), nullable = False)
    phone = db.column(db.String(100), nullable = False)
    role = db.column(db.String(100), nullable = False)

    def set_pass(self, password):
        self.password = generate_password_hash(password)
    

    def __init__(self, name, email, password, phone, role):
        self.name= name
        self.email = email
        self.set_pass(password)
        self.phone = phone
        self.role = role
    
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()