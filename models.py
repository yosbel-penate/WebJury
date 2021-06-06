from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mongoengine import Document
from mongoengine import *

class User(Document):
        name =StringField(max_length=200, required=True)
        email = StringField(max_length=200, required=True)
        password = StringField(max_length=200, required=True)
        is_active = BooleanField()
