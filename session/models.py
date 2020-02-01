from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class ActivityPost(models.Model):
	#활동사진(사진, 날짜)
	image = models.ImageField(blank=True,upload_to="session/%Y/%m/%d")
	publish_date = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=False)
	def publish(self):
		self.updated = timezone.now(); 
		self.save()


class NewsPost(models.Model):
	#유심뉴스(제목, 날짜, 작성자, 사진, 글 내용)
	#user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=120)
	#slug = models.SlugField(unique=True, blank=True) #url incoded value: hi hello -> hi-hello
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(blank=True, upload_to="session/news")
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True) #DB created time
	updated = models.DateTimeField(auto_now=True) #when click save

	#class Meta:
	#	ordering = ['-publish_date','-updated','-timestamp']

	#def get_absolute_url(self):
	#	return f"/news/{self.slug}"

	#def get_edit_url(self):
	#	return f"{self.get_absolute_url()}/edit"

	#def get_delete_url(self):
	#	return f"{self.get_absolute_url()}/delete"