from django.shortcuts import render
from django.http import HttpResponse
from .models import *
 

# Create your views HttpResponse.
def home(request):
	return render(request,'base.html')

def register(request):
	return render(request,'register.html')

def reg(request):
	u=request.POST['uname']
	p=request.POST['passw']
	t=request.POST['title']
	tx=request.POST['texts']
	obj = Person.objects.create(usern=u,passw=p,title=t,text=t)
	return render(request,'base.html')


def checkcre(request):
	uname=request.POST['uname']
	passw=request.POST['passw']
	check=uname+passw
	objects=get_object_or_404(Person,usern=uname,passw=passw)
	if(objects.DoesNotExist):
		return HttpResponse("wrong password or username")
	
		
	else:
		return render(request,'login.html',{
			'uname':uname,
			'passw':passw
			})

	