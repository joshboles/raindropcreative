from django.db import models
from taggit.managers import TaggableManager
import datetime

# Create your models here.
class Projects(models.Model):
    tags = TaggableManager