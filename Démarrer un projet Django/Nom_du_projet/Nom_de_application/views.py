from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect

def index(request):
	context = locals()
	template = "index.html"

	return render(request,template,context)