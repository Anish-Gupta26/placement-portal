from django.db import models

# Create your models here.

class Customer(models.Model):
	class Meta:
		verbose_name = 'Student'
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	class Meta:
		verbose_name = 'Companie'
	CATEGORY = (
			('A+', 'A+'),
			('A', 'A'),
			('B', 'B'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	class Meta:
		verbose_name = 'placement_entrie'
	STATUS = (
			('Pending', 'Pending'),
			# ('Out for delivery', 'Out for delivery'),
			('Completed', 'Completed'),
			)
	OPTION = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	upgrade = models.CharField(max_length=3,default="No",choices=OPTION)
	# temp = models.BooleanField(null=True)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name
