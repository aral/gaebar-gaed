from appengine_django.models import BaseModel
from google.appengine.ext import db

import logging

"""
The models here are used to test the following cases:

	* Serialization/deserialization of all datastore types
	* Reference keys and SelfReference keys.
	* Entities with regular keys and named keys
	* ListProperty of keys
	* Ancestor relationships - TODO

"""

class Profile(db.Model):
	"""
	Used to test db.SelfReferenceProperty and db.ListProperty of Keys.
	
	"""
	full_name = db.StringProperty(default="Aral Balkan")
	in_relationship_with = db.SelfReferenceProperty()
	friends = db.ListProperty(db.Key)


class GoogleAccount(db.Model):
	"""
	Used to test db.UserProperty and db.ReferenceProperty.

	"""
	user = db.UserProperty()
	profile = db.ReferenceProperty(Profile, collection_name="google_accounts")

		
class AllOtherTypes(db.Model):
	"""
	Used to test that all other data types are serialized/deserialized correctly.
	
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
	blob_property = db.BlobProperty(default=db.Blob(open('images/pink-gae.png').read()))
	text_property = db.TextProperty(default="Another lovely string.")
	category_property = db.CategoryProperty(default=db.Category("kittens"))
	link_property = db.LinkProperty(default=db.Link('http://aralbalkan.com'))
	email_property = db.EmailProperty(default='me@somewhere.com')
	geo_pt_property = db.GeoPtProperty(default=db.GeoPt(50.831096,-0.129776))
	im_property = db.IMProperty(default=db.IM("http://example.com/", "Larry97"))
	phone_number_property = db.PhoneNumberProperty(default=db.PhoneNumber("1 (206) 555-1212"))
	postal_address_property = db.PostalAddressProperty(default=db.PostalAddress("1600 Ampitheater Pkwy., Mountain View, CA"))
	rating_property = db.RatingProperty(default=97)
	

