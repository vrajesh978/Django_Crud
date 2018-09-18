# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class student(models.Model):
	roll_no = models.IntegerField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=254)
	class Meta:
		db_table="student"

class Users(models.Model):
	full_name = models.CharField(max_length=255)
	mobile_no =  models.IntegerField()
	email = models.EmailField(max_length=254)
	password = models.CharField(max_length=20)
	class meta:
		db_table="Users"