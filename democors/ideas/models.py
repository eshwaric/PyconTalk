from django.db import models

# Create your models here.
class Idea(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	up_vote = models.IntegerField(default=0)
	down_vote = models.IntegerField(default=0)
