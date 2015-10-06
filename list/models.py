

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class listObject(models.Model):
	data = models.CharField(max_length = 50)
	createDate = models.DateTimeField('date published')
	ownerName = models.CharField(max_length = 200)
	priority = models.IntegerField(default = 10)
	dropOffLocation = models.CharField(max_length = 200)
	uniqueID = models.IntegerField(default = 0)
