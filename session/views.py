from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewsModelForm, ActivityModelForm
from .models import ActivityPost,NewsPost
#GET -> RETRIEVE / LIST
#POST -> CREATE / UPDATE / DELETE

def news_list_view(request):
	qs = NewsPost.objects.all() #objects -> django manager
	context={'object_list' : qs}
	return render(request, 'news/list.html', context)

def news_detail_view(request, slug):
	obj = get_object_or_404(NewsPost, slug=slug) #handles 404exceptions in 1 line
	context={"object": obj}
	return render(request, 'news/detail.html', context)

@staff_member_required
@login_required
def news_create_view(request):
	form = NewsModelForm(request.POST or None, request.FILES)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user #set current user
		obj.save()
		form = NewsModelForm() #reinitialize
	context={
		'form' : form
	}
	return render(request, 'news/create.html', context)

@staff_member_required
@login_required
def news_update_view(request,slug):
	obj = get_object_or_404(NewsPost, slug=slug) #lookup the object
	form = NewsModelForm(request.POST or None, instance=obj)
	if form.is_valid():
	 	form.save() #update current data
	context={'form': form,"title": f"Update {obj.title}"}
	return render(request, 'news/create.html', context)


@staff_member_required
@login_required
def news_delete_view(request,slug):
	obj = get_object_or_404(NewsPost, slug=slug) #lookup the object
	if request.method == "POST":
		obj.delete()
		return redirect('../../') #redirect
	context={"object": obj}
	return render(request, 'news/delete.html', context)



######################################################UXIMACTIVITY



def activity_list_view(request):
	qs = ActivityPost.objects.all() #objects -> django manager
	context={'object_list' : qs}
	return render(request, 'activity/list.html', context)

def activity_detail_view(request, slug):
	obj = get_object_or_404(ActivityPost, slug=slug) #handles 404exceptions in 1 line
	context={"object": obj}
	return render(request, 'activity/detail.html', context)

@staff_member_required
@login_required
def activity_create_view(request):
	form = ActivityModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user #set current user
		obj.save()
		form = ActivityModelForm() #reinitialize
	context={
		'form' : form
	}
	return render(request, 'activity/create.html', context)

@staff_member_required
@login_required
def activity_update_view(request,slug):
	obj = get_object_or_404(NewsPost, slug=slug) #lookup the object
	form = ActivityModelForm(request.POST or None, instance=obj)
	if form.is_valid():
	 	form.save() #update current data
	context={'form': form,"title": f"Update {obj.title}"}
	return render(request, 'activity/create.html', context)


@staff_member_required
@login_required
def activity_delete_view(request,slug):
	obj = get_object_or_404(ActivityPost, slug=slug) #lookup the object
	if request.method == "POST":
		obj.delete()
		return redirect('../../') #redirect
	context={"object": obj}
	return render(request, 'activity/delete.html', context)
