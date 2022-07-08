from django.db import models


# class Contact_Us(models.Model):
# 	name_m = models.TextField(default = 'jaji')
# 	email_m = models.TextField(blank = True)
# 	concern_m = models.TextField(blank = True)
# 	review_m = models.TextField(blank = True)

class Customer(models.Model):
	customer_name = models.CharField(max_length=80)
	contact_no = models.CharField(max_length=11)
	customer_email = models.EmailField(max_length=80)
	City_or_Municipality = models.CharField(max_length=200)
	Province = models.CharField(max_length=200)

class meta:
	db_table = "CustomerTable"

	# def __str__(self):
	# 	return self.customer_name


# class Product(models.Model):
# 	product_choices = (
# 		('E', 'Electronics'),
# 		('F', 'Furnitures'),
# 		('D', 'Decoration'),
# 		('O', 'Others')
# 		)
# 	product_type = models.CharField(max_length=100, choices=product_choices, null=True)
# 	product_name = models.CharField(max_length=150)
# 	price = models.CharField(max_length=99999)

# 	def __str__(self):
# 		return self.product_name

class Order(models.Model):
	name_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
	product = models.CharField(max_length=999)
	quantity = models.PositiveIntegerField()
	order_date = models.DateField(auto_now_add = True)
	type_choices = (
		('SD', 'Same Day Delivery'),
		('ND', 'Normal Delivery')
		)
	delivery_type = models.CharField(max_length=100, choices=type_choices, null=True)

class meta:
	db_table = "OrderTable"
	# name = models.ForeignKey(Customer, on_delete = models.CASCADE)
	# timestamp = models.DateField(auto_now_add = True)
	# product = models.ForeignKey(Product, on_delete = models.CASCADE)
	# quantity = models.PositiveIntegerField()
	
# class Delivery(models.Model):
# 	name = models.ForeignKey(Customer, on_delete = models.CASCADE)
# 	type_choices = (
# 		('SD', 'Same Day Delivery'),
# 		('ND', 'Normal Delivery')
# 		)
# 	delivery_type = models.CharField(max_length=100, choices=type_choices, null=True)
# 	departure_date = models.DateField(auto_now_add = True)
# 	arrival_date = models.DateField(auto_now_add = True)
	
class Review(models.Model):
	name = models.ForeignKey(Customer, on_delete = models.CASCADE)
	concern_choices = (
		('R', 'Reques'),
		('Q', 'Question'),
		('C', 'Complaints'),
		('O', 'Others')
		)
	concern_type = models.CharField(max_length=100, choices=concern_choices, null=True)
	message = models.TextField(max_length=200)

