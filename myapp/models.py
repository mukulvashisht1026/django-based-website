from django.db import models


class Credentials(models.Model):
	passw=models.CharField(max_length=25)
	usern=models.CharField(unique=True,max_length=20)
	def __str__(self):
		return (self.usern+self.passw)

	
	
	#address=models.CharField(max_length=200)
	#tech=models.CharField(max_length=500)
	#=models.CharField(max_length=30)
	#name=models.CharField(max_length=30)
	

class Person(models.Model):
	title=models.CharField(max_length=100)
	text=models.CharField(max_length=2000)
	userpa=models.ForeignKey(Credentials,on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return (self.title)

	

# Create your models here.