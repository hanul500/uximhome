#from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsModelForm, ActivityModelForm
from .models import ActivityPost,NewsPost

#########################################################
#UXIMNEWS

def news_list_view(request):
	context={'object_list' : qs}
	return render(request, 'news/list.html', context)

def news_detail_view(request, slug):
	#retrieve 1 object -> detail view 
	obj = get_object_or_404(BlogPost, slug=slug)
	context={"object": obj}
	return render(request, 'news/detail.html', context)

#@staff_member_required
#@login_required
def news_create_view(request):
	form = NewsModelForm(request.POST or None, request.FILES)
	if form.is_valid():
		form.save()

	context={'form' : form}
	return render(request, 'news/create.html', context)

#@staff_member_required
#@login_required
def news_update_view(request,slug):
	#first retrieve obj
	obj = get_object_or_404(BlogPost, slug=slug) #lookup the object
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
	 	form.save()
	context={'form': form,"title": f"Update {obj.title}"}
	return render(request, 'form.html', context)

#@staff_member_required
#@login_required
def news_delete_view(request,slug):
	#first retrieve obj
	obj = get_object_or_404(BlogPost, slug=slug)
	if request.method == "POST":
		obj.delete()
		return redirect("../")
	context={"object": obj}
	return render(request, 'news/delete.html', context)


#####################################################
#UXIMACTIVITY
