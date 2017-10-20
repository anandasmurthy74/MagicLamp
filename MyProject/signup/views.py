from django.http.response import HttpResponse
from signup.models import user


def index(Reqest):
	users = user.objects.all()
	html = ''
	for user in users:
		url = '/signup/' + str(user.userId) + '/'
		html += '<a href="' + url + '">' + user.username + '</a><br>'
    return HttpResponse(html)

def details(request,userId):
	return HttpResponse('<h2> The details of the user are '+ str(userId) + '.</h2>')
