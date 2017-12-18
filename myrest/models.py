from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
	owner = models.ForeignKey('auth.User', related_name='book', on_delete=models.CASCADE)
		