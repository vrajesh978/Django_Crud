# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from crudapp.models import student

# Register your models here.
# for admin crud 
# doing this, you can handle data from admin!!
admin.site.register(student)