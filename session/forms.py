from django import forms
from .models import ActivityPost,NewsPost

class NewsModelForm(forms.ModelForm):
	class Meta:
		model = NewsPost
		fields = ['title', 'content','image']
		#fields to be used (bring from model)

class ActivityModelForm(forms.ModelForm):
	class Meta:
		model = ActivityPost
		fields = ['image']
		#fields to be used