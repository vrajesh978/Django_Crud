from django import forms  
from crudapp.models import student,Users
     
class StudentForm(forms.ModelForm):  
	class Meta:  
		model = student
		fields = "__all__"  

class loginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Users
		fields = ['email', 'password']

class registerForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Users
		fields = "__all__"