from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.template.loader import get_template
from django.forms.models import modelformset_factory
from django.views.generic.edit import FormView
from .models import *
from .forms import *


def project_page(request):
	obj = Project.objects.all()
	context = {"title": "안녕 유심", "obj":obj}
	return render(request, "project/project.html", context)


def project_create(request):
	form = ProjectForm(request.POST or None , request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			print(form.is_valid())
			obj = form.save(commit=False)
			obj.project_user = request.user
			obj.project_main_image = request.FILES.get('main_image')
			obj.save()

			for f in request.FILES.getlist('image'):
				image = Project_Image()
				image.project=obj
				image.project_image = f
				image.save()

		form = ProjectForm()
	template = 'project/project_create.html'
	context = {"form":form}
	return render(request, template, context)


def project_detail(request, project_name):
	obj = get_object_or_404(Project, project_name=project_name)
	images = Project_Image.objects.all().filter(project=obj)
	template = 'project/project_detail.html'
	context = {"obj":obj, "images": images}
	return render(request, template, context)


def project_update(request, project_name):
	proj_obj = get_object_or_404(Project, project_name=project_name)
	form = ProjectForm(request.POST or None , request.FILES or None, instance=proj_obj)
	if request.method == 'POST':
		if form.is_valid():
			print(form.is_valid())
			obj = form.save(commit=False)
			obj.project_user = request.user
			obj.project_main_image = request.FILES.get('main_image')
			obj.save()

			for f in request.FILES.getlist('image'):
				image = Project_Image()
				image.project=obj
				image.project_image = f
				image.save()

		form = ProjectForm()
	template = 'project/project_update.html'
	context = {"form":form,'proj_obj':proj_obj}
	return render(request, template, context)


def project_delete(request, project_name):
	proj_obj = get_object_or_404(Project, project_name=project_name)
	if request.method == 'POST':
		proj_obj.delete()
	template = 'project/project_delete.html'
	context = {'proj_obj':proj_obj}
	return render(request, template, context)
