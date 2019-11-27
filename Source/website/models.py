"""
This file represents each database using classes.
""" 

from django.db import models
from django.utils.timezone import make_aware

# Create your models here.
class User(models.Model):
	"""
    This class stores all the user data when an user registers and also the updates.
    """ 
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	email = models.EmailField()
	balance = models.DecimalField(max_digits=7, decimal_places=2)
	firstname = models.CharField(max_length=56)
	lastname = models.CharField(max_length=45)
	cellphone = models.CharField(max_length=14)
	address = models.CharField(max_length=255)
	town = models.CharField(max_length=45)
	post_code = models.CharField(max_length=45)
	country = models.CharField(max_length=45)
	
	def __str__(self):
		return "ID:" + str(self.pk) + " " + self.username + " " + self.email

class Product(models.Model):
	"""
    Whenever a new product is put up for auction, the details are stored as an object of this class.
    """ 
	CATEGORIES = (
		('HH','Household'),
		('EL','Electronics'),
		('BS','Books and Study Material')
	)
	
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	base_price = models.IntegerField()
	time_starting = models.DateTimeField()
	category = models.CharField(
		max_length=2,
		choices=CATEGORIES
	)
	image = models.ImageField(upload_to='images/')
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return "ID:" + str(self.pk) + " " + self.title

class Auction(models.Model):
	"""
	This class stores the auction details of a specific product(base price, start time, end time, etc.)
	"""
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	################
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	################
	base_price = models.IntegerField()
	number_of_bids = models.IntegerField()
	time_starting = models.DateTimeField()
	time_ending = models.DateTimeField()
	
	def __str__(self):
		return "ID:" + str(self.pk) + " PRODUCT_ID:" + str(self.product_id)

class Watchlist(models.Model):
	"""
	This class stores the info of all the products an user is watching.
	"""
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	
	def __str__(self):
		return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + str(self.auction_id)

class Bid(models.Model):
	"""
	This class stores the highest bid made on a product and the user who placed the bid.
	"""
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	bid_time = models.DateTimeField()
	
	def __str__(self):
		return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + \
			str(self.auction_id) + " " + str(self.bid_time) 

class Chat(models.Model):
	"""
	This class stores the messages posted on a product by an user.
	"""
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.TextField()
	time_sent = models.DateTimeField()

	def __str__(self):
		return "AUCTION_ID:" + str(self.auction_id) + " USER_ID:" + str(self.user_id)

