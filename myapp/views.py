from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import RegForm,login_form
from django.urls import reverse
 

# Create your views HttpResponse.
'''def home(request):
	return render(request,'base.html')
'''
'''def register(request):
	return render(request,'register.html')
'''
def reg(request):	
	if request.method=='POST':
		form = RegForm(request.POST)
	
		if(form.is_valid()):
			print("hello world")
			a=form.save(commit=False)

			a.user=request.user
			a.save()
			
			return HttpResponseRedirect(reverse('login'))
	else:
	
		form = RegForm()
	return render(request,'register.html',{'form':form})

def checkcre(request):
	if request.method=='POST':
		form = login_form(request.POST)
		if(form.is_valid()):
			user_n= form.cleaned_data['user_name']
			pass_w= form.cleaned_data['pass_word']

			try:
				check_cre=Credentials.objects.get(usern=user_n,passw=pass_w)
			except (KeyError, Credentials.DoesNotExist):
				return HttpResponse("worng username and password")

			else:
				return HttpResponse("correct answer you win!!!!!")

	else:

		form = login_form()
	return render(request,'base.html',{'form':form})
	
