"""
Test value constants for populating the database and testing against.

"""

import datetime
from google.appengine.ext import db


STRING_PROPERTY = 'A lovely string.'
BOOLEAN_PROPERTY = True
INTEGER_PROPERTY = 42
FLOAT_PROPERTY = 36.8
DATE_TIME_PROPERTY = datetime.datetime(2009, 1, 20, 12, 00, 00)
DATE_PROPERTY = datetime.datetime(2009, 1, 20, 12, 00, 00)
TIME_PROPERTY = datetime.datetime(2009, 1, 20, 12, 00, 00)
LIST_PROPERTY = [1,2,3]
STRING_LIST_PROPERTY = ['hello', 'world']
BLOB_PROPERTY = db.Blob(open('images/pink-gae.png').read())
TEXT_PROPERTY = 'Another lovely string.'
CATEGORY_PROPERTY = db.Category("kittens")
LINK_PROPERTY = db.Link('http://aralbalkan.com')
EMAIL_PROPERTY = 'me@somewhere.com'
GEO_PT_PROPERTY = db.GeoPt(50.831096,-0.129776)
IM_PROPERTY = db.IM("http://example.com/", "Larry97")
PHONE_NUMBER_PROPERTY = db.PhoneNumber("1 (206) 555-1212")
POSTAL_ADDRESS_PROPERTY = db.PostalAddress("1600 Ampitheater Pkwy., Mountain View, CA")
RATING_PROPERTY = db.RatingProperty(default=97)