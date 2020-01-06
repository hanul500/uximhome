from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.template.loader import get_template


def home_page(request):
	context = {"title": "안녕 유심"}
	return render(request, "home.html", context)