# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=77)
	notes = models.TextField()
	created = models.DateTimeField()

from django.contrib import admin

admin.site.register(Task)

