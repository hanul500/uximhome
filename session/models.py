from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL #the only way

class ActivityPost(models.Model):
	#활동사진(사진, 날짜)
	image = models.ImageField(blank=True,upload_to="session/activity")
	publish_date = models.DateTimeField(auto_now=False)
	updated = models.DateTimeField(auto_now=False)
	def publish(self):
		self.updated = timezone.now(); 
		self.save()


class NewsPost(models.Model):
	#유심뉴스(제목, 날짜, 작성자, 사진, 글 내용)
	slug = models.SlugField(unique=True, blank=True, null=False)
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #bind a model(user) to another(newpost)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(blank=True, upload_to="session/news")
	publish_date = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now=True) #when click save

	#def get_absolute_url(self):
	#	return f"/news/{self.slug}"

	#def get_edit_url(self):
	#	return f"{self.get_absolute_url()}/edit"

	#def get_delete_url(self):
	#	return f"{self.get_absolute_url()}/delete"