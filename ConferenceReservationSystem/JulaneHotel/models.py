from django.db import models

# Create your models here.

class Rooms(models.Model):
	roomtype = models.CharField(max_length=20)
	dateofuse = models.Datefield()
	timeslot = models.CharField(max_length=20)
	price = models.IntegerField()

	class meta:
		db_table = 'Rooms'

class Customer(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	contactnum = models.IntegerField()

	class meta:
		db_table = 'Customer'

class Reservation(models.Model):
	dateofuse = models.CharField(max_length=20)
	timeslot = models.CharField(max_length=20)
	roomtype = models.CharField(max_length=20)
	

	class meta:
		db_table = 'Reservation'

class Admin(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	class meta:
		db_table = 'Admin'
