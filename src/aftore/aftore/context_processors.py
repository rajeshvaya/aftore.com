from django.conf import settings

def disqus(request):
	if settings.DEBUG:
		return {
			'DISQUS':{
				'SHORTNAME': 'aftore',
				'IDENTIFIER_PREFIX': 'aftoretest'
			}
		}
	else:
		return {
			'DISQUS':{
				'SHORTNAME': 'aftore',
				'IDENTIFIER_PREFIX': 'aftore'
			}
		}

def globals(request):
	return{
		'GLOBALS':{
			'BASE_URL': settings.BASE_URL
		}
	}

	

