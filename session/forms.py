from django import forms
from .models import ActivityPost,NewsPost

class NewsModelForm(forms.ModelForm):
	class Meta:
		model = NewsPost
		fields = ['title', 'content','image','slug']
		#fields to be used (django brings from model)

class ActivityModelForm(forms.ModelForm):
	class Meta:
		model = ActivityPost
		fields = ['image']
		#fields to be used (django brings from model)