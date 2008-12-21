from appengine_django.models import BaseModel
from google.appengine.ext import db

class Simple(db.Model):
	life_is_like = db.StringProperty(default='a box of chocolates')

