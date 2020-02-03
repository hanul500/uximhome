from django.db import models
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
import datetime
# Create your models here.

User = settings.AUTH_USER_MODEL
class Project(models.Model):
	def __str__(self):
		return str(self.project_name)
	project_name = models.CharField(null=True,max_length=120)
	project_member = models.CharField(null=True, blank=True,max_length=120)
	project_period = models.CharField(null=True, blank=True,max_length=120)
	project_text = models.TextField(null=True, blank=True)
	project_main_image = models.ImageField(blank=True, upload_to='project_main_image/')
	project_user = models.ForeignKey(User,default=1, null=True, blank=True, on_delete=models.CASCADE)


class Project_Image(models.Model):
	def __str__(self):
		return str(self.project.project_name)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	project_image = models.ImageField(blank=True, upload_to='project/')