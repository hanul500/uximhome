from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL #the only way

class ActivityPost(models.Model):
	#활동사진(사진, 날짜)
	slug = models.SlugField(unique=True, blank=True, null=False)
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #bind a model(user) to another(newpost)
	image = models.ImageField(blank=True,upload_to="session/activity")

	publish_date = models.DateTimeField(auto_now_add=True, null=True) #when added to DB
	updated = models.DateTimeField(auto_now=True) #when click save

		#order of qs
	class Meta:
		ordering = ['-publish_date', '-updated']

	def get_absolute_url(self):
		return f"{self.slug}"



class NewsPost(models.Model):
	#유심뉴스(제목, 날짜, 작성자, 사진, 글 내용)
	slug = models.SlugField(unique=True, blank=True, null=False)
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #bind a model(user) to another(newpost)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(blank=True, upload_to="session/news")

	publish_date = models.DateTimeField(auto_now_add=True, null=True) #when added to DB
	updated = models.DateTimeField(auto_now=True) #when click save

	#order of qs
	class Meta:
		ordering = ['-publish_date', '-updated']

	def get_absolute_url(self):
		return f"{self.slug}"