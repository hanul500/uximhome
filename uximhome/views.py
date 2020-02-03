from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.template.loader import get_template


def home_page(request):
	context = {"title": "UXIM HOMEPAGE"}
	return render(request, "home.html", context)

def session_page(request):
	context = {"title": "SESSION PAGE"}
	return render(request, "session.html",context)

def about_page(request):
	context = {"title": "ABOUT PAGE"}
	return render(request, "about.html", context)

def contact_page(request):
	context = {"title": "CONTACT PAGE"}
	return render(request, "contact.html", context)

def project_page(request):
	context = {"title": "PROJECT PAGE"}
	return render(request, "project.html")