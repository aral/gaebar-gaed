from appengine_django.models import BaseModel
from google.appengine.ext import db

import logging

"""
Test cases covered:

1. All datastore types

2. Reference keys

3. Entities with regular keys

4. Entities with named keys

5. ListProperty of keys

6. Ancestor relationships


"""

class FirstModel(db.Model):
	"""
	Used in test 2 (reference keys).

	"""
	string_property = db.StringProperty(default="Herbert")



class AllTypes(db.Model):
	"""
	Used in test 1 (all datastore types).
	
	"""
	string_property = db.StringProperty(default="A lovely string.")
	boolean_property = db.BooleanProperty(default=True)
	integer_property = db.IntegerProperty(default=42)
	float_property = db.FloatProperty(default=36.8)
	date_time_property = db.DateTimeProperty(auto_now_add=True)
	date_property = db.DateProperty(auto_now_add=True)
	time_property = db.TimeProperty(auto_now_add=True)
	list_property = db.ListProperty(int, default=[1,2,3])
	string_list_property = db.StringListProperty(default=['hello', 'world'])
	reference_property = db.ReferenceProperty(FirstModel)
	self_reference_property = db.SelfReferenceProperty()
	user_property = db.UserProperty()
	blob_property = db.BlobProperty(default=db.Blob(open('images/pink-gae.png').read()))
	text_property = db.TextProperty(default="Another lovely string.")
	category_property = db.CategoryProperty(default=db.Category("kittens"))
	link_property = db.LinkProperty('http://aralbalkan.com')
	email_property = db.EmailProperty(default='me@somewhere.com')
	geo_pt_property = db.GeoPtProperty(default=db.GeoPt(50.831096,-0.129776))
	im_property = db.IMProperty(default=db.IM("http://example.com/", "Larry97"))
	phone_number_property = db.PhoneNumberProperty(default=db.PhoneNumber("1 (206) 555-1212"))
	postal_address_property = db.PostalAddressProperty(default=db.PostalAddress("1600 Ampitheater Pkwy., Mountain View, CA"))
	rating_property = db.RatingProperty(97)
	

	