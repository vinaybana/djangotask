from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from autoslug import AutoSlugField

# Create your models here.

gender = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
slots = (("slot1", "slot1"), ("slot2", "slot2"), ("slot3", "slot3"), ("slot4", "slot4"))
status = (("Active", "Active"), ("Inactive", "Inactive"), ("Delete", "Delete"))

class User(AbstractUser):
	mobile = models.CharField(max_length=15, blank=True, null=True)
	gender = models.CharField(max_length=6, choices=gender, default='Male')
	dob = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to='user/', blank=True, null=True)
	role = models.CharField(max_length=55)

	class Meta:
		verbose_name_plural = "01. Users"


class Category(models.Model):
	title= models.CharField(max_length=200)
	text=models.TextField()
	slug = AutoSlugField(populate_from='title', max_length=160, editable=True)
	parent=models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
	created_date = models.DateTimeField(default = timezone.now)

	class Meta:
		verbose_name_plural = "categories" 

	def __str__(self):
		return self.title

	def slugify_function(self, content):
		return content.replace('_', '-').lower()

class Tag(models.Model):
	title = models.CharField(blank=True, max_length=200)
	text=models.TextField(default=True)
	slug = AutoSlugField(populate_from='title', max_length=160, editable=True)
	created_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title

	def slugify_function(self, content):
		return content.replace('_', '-').lower()

class Post(models.Model):
	tag = models.ManyToManyField('Tag')
	category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_query_name="posts")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	slug = AutoSlugField(populate_from='title', max_length=160, editable=True)
	

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title 

	def slugify_function(self, content):
		return content.replace('_', '-').lower()

class Appoitment(models.Model):
	name = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateField()
	slot1 = models.TimeField(default='09:00:00')
	slot2 = models.TimeField(default='11:00:00')
	slot3 = models.TimeField(default='14:00:00')
	slot4 = models.TimeField(default='16:00:00')
	slot = models.CharField(max_length=20, choices=slots, default='slot1')

	def __str__(self):
		return str(self.name)