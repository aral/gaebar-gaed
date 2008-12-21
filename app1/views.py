import logging
import sys

from google.appengine.api import users
from google.appengine.ext import db

from google.appengine.api import datastore_types

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
			
	stephanie = app1_models.Profile(key_name="stephalicious")
	stephanie.full_name = "Stephanie King"
	stephanie.put()
	
	paul = app1_models.Profile()
	paul.full_name = "Paul Booth"
	paul.put()
	
	# Test reference properties with named keys, and ListProperty of Keys:
	aral = app1_models.Profile()
	aral.in_relationship_with = stephanie
	aral.friends = [stephanie.key(), paul.key()]
	aral.put()	

	# Test reference properties with regular keys
	stephanie.in_relationship_with = aral
	stephanie.put()
		
	# Test db.UserProperty and db.ReferenceProperty with regular keys.
	google_account_1 = app1_models.GoogleAccount()
	google_account_1.user = user
	google_account_1.profile = aral
	google_account_1.put()

	# Test db.UserProperty and db.ReferenceProperty with regular keys.
	google_account_2 = app1_models.GoogleAccount()
	google_account_2.user = user
	google_account_2.profile = stephanie
	google_account_2.put()	
	
	# To test all other properties.
	all_types_1 = app1_models.AllOtherTypes()
	all_types_1.put()
		
	return HttpResponse('Successfully populated the datastore.')
		

def run_tests(request):
	"""
	Runs the functional tests.
	
	"""
	
	if not users.is_current_user_admin():
		return HttpResponseRedirect('/?auth=False')
	
	error_message = None
	
	# Test get Stephanie.
	stephanie_test = test_get_stephanie()
	if not stephanie_test[0]:
		return error_message(stephanie_test[1])
	else:
		stephanie = stephanie_test[1]

	# Test get Aral.
	aral_test = test_get_aral()
	if not aral_test[0]:
		return error_message(aral_test[1])
	else:
		aral = aral_test[1]

	# Test get Paul.
	paul_test = test_get_paul()
	if not paul_test[0]:
		return error_message(paul_test[1])
	else:
		paul = paul_test[1]
	
	# Test ReferenceProperty with regular keys.
	try:
		if not (type(aral.google_accounts[0]) == app1_models.GoogleAccount):
			return err('ReferenceProperty fail with regular keys. aral.google_accounts[0] not == app1_models.GoogleAccount')
	except:
		return err('ReferenceProperty fail with regular keys. Exception encountered while referencing aral.google_accounts[0]')

	# Test ReferenceProperty with named keys.
	try:
		if not (type(stephanie.google_accounts[0]) == app1_models.GoogleAccount):
			return err('ReferenceProperty fail with named keys. stephanie.google_accounts[0] not == app1_models.GoogleAccount')
	except:
		return err('ReferenceProperty fail with named keys. Exception encountered while referencing aral.google_accounts[0]')

			
	# Test SelfReferenceProperty with named keys.
	if not aral.in_relationship_with.full_name == stephanie.full_name:
		return err('SelfReferenceProperty fail with named keys. aral.in_relationship_with not == stephanie.')
		
	# Test SelfReferenceProperty with regular keys.
	if not stephanie.in_relationship_with.full_name == aral.full_name:
		return err('SelfReferenceProperty fail with regular keys. stephanie.in_relationship_with not == aral.')
			
		
	# Test ListProperty.
	try:
		arals_friends = aral.friends
		num_arals_friends = len(arals_friends)
		
		# Test number of items.
		if not num_arals_friends == 2:
			return err('ListProperty test fail. arals_friends should be 2, instead we got ' + str(num_arals_friends))
			
		# Test type of items.
		for arals_friend in arals_friends:
			if not (type(arals_friend) == datastore_types.Key):
				return err('ListProperty test fail. Type of arals_friends is not datastore_types.Key.')
			
		# Test that they are actually the keys for the right entities.
		stephanie_key = arals_friends[0]
		paul_key = arals_friends[0]	
		
		stephanie_from_key = app1_models.Profile.get(stephanie_key)
		# paul_from_key = app1_models.Profile.get(paul_key)
		
		if not (stephanie_from_key.full_name == stephanie.full_name):
			return err('ListProperty test fail. stephanie_from_key.full_name not == stephanie.full_name.')
		
		# if not (paul_from_key.full_name == paul.full_name):
		# 	return err('ListProperty test fail. paul_from_key.full_name not == paul.full_name.')
			
			
	except:
		return err('ListProperty test fail. Exception encountered while referencing aral.friends.')


	
	
	
	
	return HttpResponse('All tests ran successfully.')

#
# Helpers
#

def err(msg):
	return HttpResponse('Error %s ' % msg)
		
#
# Tests
#		
		
def test_get_stephanie():
	"""
	Returns Stephanie or error.
	"""
	
	try:
		stephanie = app1_models.Profile.get_by_key_name('stephalicious')
	except:
		error_message = 'Test Get Stephanie failed while trying to get_by_key_name.'
		
	if not stephanie:
		error_message = 'Test Get Stephanie get_by_key_name lookup returned None.'
	
	return (False, error_message) if 'error_message' in locals() else (True, stephanie)


def test_get_aral():
	"""
	Returns Aral or error.
	"""
	
	try:
		aral = app1_models.Profile.all().filter('full_name =', 'Aral Balkan').get()
	except:
		error_message = 'Test Get Aral failed during query.'
		
	if not aral:
		error_message = 'Test Get Aral returned None.'
	
	return (False, error_message) if 'error_message' in locals() else (True, aral)
	
	
def test_get_paul():
	"""
	Returns Paul or error.
	"""
	
	try:
		paul = app1_models.Profile.all().filter('full_name =', 'Paul Booth').get()
	except:
		error_message = 'Test Get Paul failed during query.'
		
	if not paul:
		error_message = 'Test Get Paul returned None.'
	
	return (False, error_message) if 'error_message' in locals() else (True, paul)
