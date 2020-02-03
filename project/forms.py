from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
	project_name = forms.CharField()
	project_member = forms.CharField()
	project_period = forms.CharField()
	project_text = forms.Textarea()


	class Meta:
		model = Project
		fields = ['project_name', 'project_member' , 'project_period', 'project_text']

class ProjectImageForm(forms.ModelForm):
	project_image = forms.ImageField()

	class Meta:
		model = Project_Image
		fields = ['project_image',]



class ImageForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        