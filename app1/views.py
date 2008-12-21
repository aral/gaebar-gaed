import logging

from google.appengine.api import users
from google.appengine.ext import db

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from app1 import models as app1_models
from app2 import models as app2_models

def index(request):
	response = '<h1>Gaebar Test App for Google App Engine Helper</h1>'
	
	if 'auth' in request.REQUEST:
		auth = request.REQUEST['auth']
		if auth == 'False':
			response += '<p><strong>You must sign in as administrator to do that.</strong></p>'
	
	if users.is_current_user_admin():
		account_link_url = users.create_logout_url('/')
		account_link_label = 'Sign out.'
		
		response += '<p>Welcome, administrator!</p><p><a href="/populate-datastore/">Populate the datastore.</a></p>'
		
	else:
		account_link_url = users.create_login_url('/')
		account_link_label = 'Sign in as administrator to continue.'
		
	account_link = '<a href="%s">%s</a>' % (account_link_url, account_link_label)
	
	response += account_link
		
	return HttpResponse(response)


def populate_datastore(request):
	"""
	Populate the datastore with the functional test data.
	
	"""
	if not users.is_current_user_admin():
		return HttpResponseRedirect('/?auth=False')
		
	user = users.get_current_user()
		
	# Along with all_types_1, to test reference_property.
	first_model = app1_models.FirstModel()
	first_model.put()
	
	# To test all other properties.
	all_types_1 = app1_models.AllTypes()
	all_types_1.reference_property = first_model
	all_types_1.user_property = user
	all_types_1.put()
	
	# To test self_reference_property.
	all_types_2 = app1_models.AllTypes()
	all_types_2.reference_property = first_model
	all_types_2.user_property = user
	all_types_2.self_reference_property = all_types_1
	all_types_2.put()
	
	
		
	return HttpResponse('Populated the datastore.')
		
	