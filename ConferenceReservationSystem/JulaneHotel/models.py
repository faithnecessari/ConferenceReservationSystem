from django.db import models

# Create your models here.

class Rooms(models.Model):
	roomtype = models.CharField(max_length=20)
	timeslot = models.CharField(max_length=20)
	price = models.IntegerField()

	class meta:
		db_table = 'Rooms'
