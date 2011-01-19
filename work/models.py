from django.db import models
import datetime
import os

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=64)
	order = models.IntegerField()
	active = models.BooleanField()
	modified = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.name
		
class Photo(models.Model):
	project = models.ForeignKey(Project, related_name="photo_set")
	description = models.TextField(blank=True, null=True)
	file = models.FileField(upload_to="project_photo")
	order = models.IntegerField()
	
	def __unicode__(self):
		return os.path.split(self.file.name)[1]