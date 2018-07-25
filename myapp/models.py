from django.db import models



	
	#address=models.CharField(max_length=200)
	#tech=models.CharField(max_length=500)
	#=models.CharField(max_length=30)
	#name=models.CharField(max_length=30)
	

class Person(models.Model):
	passw=models.CharField(max_length=20)
	usern=models.CharField(max_length=20)
	title=models.CharField(unique=True,max_length=100,blank=False,null=True)
	text=models.TextField(max_length=2000,blank=False,null=True)
	def __str__(self):
		return (self.usern+self.passw)


	

# Create your models here.