import logging

from google.appengine.api import users
from google.appengine.ext import db

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from app1 import models
from app2 import models

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
		
	return HttpResponse('Populate datastore.')
		
	