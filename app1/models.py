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
	string_property = db.StringProperty(default=consts.STRING_PROPERTY)
	boolean_property = db.BooleanProperty(default=consts.BOOLEAN_PROPERTY)
	integer_property = db.IntegerProperty(default=consts.INTEGER_PROPERTY)
	float_property = db.FloatProperty(default=consts.FLOAT_PROPERTY)
	date_time_property = db.DateTimeProperty(default=consts.DATE_TIME_PROPERTY)
	date_property = db.DateProperty(default=consts.DATE_PROPERTY)
	time_property = db.TimeProperty(default=consts.TIME_PROPERTY)
	list_property = db.ListProperty(int, consts.LIST_PROPERTY)
	string_list_property = db.StringListProperty(default=consts.STRING_LIST_PROPERTY)
	blob_property = db.BlobProperty(default=consts.BLOB_PROPERTY)
	text_property = db.TextProperty(default=consts.TEXT_PROPERTY)
	category_property = db.CategoryProperty(default=consts.CATEGORY_PROPERTY)
	link_property = db.LinkProperty(default=consts.LINK_PROPERTY)
	email_property = db.EmailProperty(default=consts.EMAIL_PROPERTY)
	geo_pt_property = db.GeoPtProperty(default=consts.GEO_PT_PROPERTY)
	im_property = db.IMProperty(default=consts.IM_PROPERTY)
	phone_number_property = db.PhoneNumberProperty(default=consts.PHONE_NUMBER_PROPERTY)
	postal_address_property = db.PostalAddressProperty(default=consts.POSTAL_ADDRESS_PROPERTY)
	rating_property = db.RatingProperty(default=consts.RATING_PROPERTY)
	



