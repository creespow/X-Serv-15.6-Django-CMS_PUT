from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from models import Page

# Create your views here.
@csrf_exempt
def cms (request, resource):
	if request.method == 'GET':
		try:
			page = Page.objects.get(name = resource)
			return HttpResponse(page.page)
		except Page.DoesNotExist:
			return HttpResponseNotFound ("Page not Found")

	elif request.method == 'PUT':
		newPage = Page(name = resource, page = request.body)
		newPage.save()
		return HttpResponse ("Added succesfull")
		
	else:
		return HttpResponse(status=400)