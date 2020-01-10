from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		#get_queryset() = BlogPost.objects : does the same thing
		return self.filter(publish_date__lte=now)


class BlogPostManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()

class BlogPost(models.Model):
	#id = models.IntegerField() -> default value
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True, blank=True) #url incoded value: hi hello -> hi-hello
	content = models.TextField(null=True, blank=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True) #DB created time
	updated = models.DateTimeField(auto_now=True) #when click save

	objects = BlogPostManager()

	class Meta:
		ordering = ['-publish_date','-updated','-timestamp']

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"