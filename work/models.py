from django.db import models
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

	def get_primary_photo(self):
		if self.photo_set.count():
			return self.photo_set.all()[0]
		return None
		
	class Meta:
		ordering = "order"

class Photo(models.Model):
	project = models.ForeignKey(Project, related_name="photo_set")
	description = models.TextField(blank=True, null=True)
	file = models.FileField(upload_to="project_photo")
	order = models.IntegerField()
	
	class Meta:
		ordering = "order"

	def __unicode__(self):
		return os.path.split(self.file.name)[1]