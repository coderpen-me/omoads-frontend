from __future__ import unicode_literals

from django.db import models

# Create your models here.


TYPE_CHOICES = (
	('gantry', 'Gantry'),
	('unipole', 'Unipole'),
)

LIGHTED_CHOICES = (
	('f', 'Front Lit'),
	('b', 'Back Lit'),
	('n', 'Not Lighted'),
)

DIMENSION_CHOICES = (
	('0', '50x10'),
	('1', '40x10'),
	('2', '30x10'),
	('3', '20x10'),
)



class Author(models.Model):
	salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	def __str__(self):
		return(self.title)

class Banner(models.Model):
	banner_id = models.CharField( max_length = 200, unique=True )
	owner_id = models.CharField( max_length = 200 ) 
	banner_region = models.CharField( max_length = 200 )
	banner_type = models.CharField( max_length=100, choices = TYPE_CHOICES, default= 'gantry')
	banner_lighted = models.CharField( max_length=100, choices = LIGHTED_CHOICES, default= 'n' )
	banner_dimensions = models.CharField( max_length=100, choices = DIMENSION_CHOICES, default= '0')
	banner_cost = models.DecimalField( max_digits = 12, decimal_places = 3 )
	banner_lattitude = models.DecimalField( max_digits = 12, decimal_places = 9 )
	banner_longitude = models.DecimalField( max_digits = 12, decimal_places = 9 )

	def __str__(self):
		return '%s %s %s %s' % (self.banner_region, self.banner_lighted, self.banner_dimensions, self.banner_cost)