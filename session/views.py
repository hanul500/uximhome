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

#wrappers
@staff_member_required
@login_required
def news_create_view(request):
	form = NewsModelForm(request.POST or None, request.FILES)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		#form.save() #modelform only needs ".save"
		form = NewsModelForm() #reinitialize
	context={
		'form' : form
	}
	return render(request, 'news/create.html', context)

#wrappers
@staff_member_required
@login_required
def news_update_view(request,slug):
	#first retrieve obj
	obj = get_object_or_404(NewsPost, slug=slug) #lookup the object
	form = NewsModelForm(request.POST or None, instance=obj)
	if form.is_valid():
	 	form.save()
	context={'form': form,"title": f"Update {obj.title}"}
	return render(request, 'news/detail.html', context)

#wrappers
@staff_member_required
@login_required
def news_delete_view(request,slug):
	obj = get_object_or_404(NewsPost, slug=slug)
	#first retrieve obj
	if request.method == "POST":
		#confirm
		obj.delete()
		return redirect('../../')
	context={"object": obj}
	return render(request, 'news/delete.html', context)


######################################################UXIMACTIVITY
