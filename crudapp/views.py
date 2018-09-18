# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, redirect, get_object_or_404,render
from django.http import HttpResponse 
from crudapp.form import StudentForm,loginForm,registerForm
from crudapp.models import student,Users
from django.contrib.messages import error

# Create your views here.
def users(request):
	if request.method=='POST':
		form=StudentForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form = StudentForm()
	return render(request,"index.html",{'form':form})


def login(request):
	if request.method=='POST':
		form = loginForm(request.POST)
		if form.is_valid():
			try:
				email = form.cleaned_data['email'] # getting specific value from form
				password = form.cleaned_data['password'] # getting specific value from form
				users = Users.objects.filter(email=email).filter(password=password)
				user_list = users.values() # getting all the values from model (db)
				if(user_list):
					return redirect("/show")
				else:
					error(request, 'either email or password is wrong')
					return redirect("/login")
			except:
				pass
	else:
		form = loginForm()
	return render(request,"login.html",{'form':form})

def register(request):
	if request.method=='POST':
		form=registerForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form = registerForm()
	return render(request,"register.html",{'form':form})

def show(request):
	students = student.objects.all()
	return render(request,"show.html",{'students':students})

def edit(request,pk):
	students = get_object_or_404(student, pk=pk)
	return render(request,"edit.html",{'student':students})

def update(request,pk):
	students = get_object_or_404(student, pk=pk)
	form = StudentForm(request.POST,instance = students)
	if form.is_valid():
		try:
			form.save()
			return redirect("/show")
		except:
			pass
	return render(request,'edit.html',{'student':students})

def delete(request,pk):
	students = get_object_or_404(student, pk=pk)
	students.delete()
	return redirect("/show")