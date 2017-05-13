from django.db import models

# Create your models here.
class Info(models.Model):
	Name = models.CharField(max_length=140)
	Number = models.IntegerField()
	def __str__(self):
		return self.Name
