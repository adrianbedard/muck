# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
#ownerName = models.TextField(max_length = 100, default = ' ')

class Info(models.Model):
	ownerName = models.TextField(max_length = 100)
	schoolName = models.TextField(max_length = 100)
	datum = models.FileField(upload_to='documents/%Y/%m/%d')
	#timeLapse = models.FileField(upload_to='documents/%Y/%m/%d')
	printCompleted = models.BooleanField(default = False)
	password = models.TextField(max_length = 50)