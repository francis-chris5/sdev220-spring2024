from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homePage(request):
	page = "<!DOCTYPE html><html><head></head>"
	page += "<body>"
	page += "<h3> Hello World!!! </h3>"
	page += "<p>this is our first django example</p>"
	page += "</body></html>"
	return HttpResponse(page)


