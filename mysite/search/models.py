
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.translation import gettext as _

# Create your models here.

STATUS_CHOICES = (
	('available', 'Available'),
	('booked', 'Booked'),
)


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
	owner_id = models.ForeignKey( Agency, on_delete=models.CASCADE ) 
	banner_facing = models.CharField( max_length = 200 )
	banner_type = models.CharField( max_length=100, choices = TYPE_CHOICES, default= 'gantry')
	banner_lighted = models.CharField( max_length=100, choices = LIGHTED_CHOICES, default= 'n' )
	banner_dimensions = models.CharField( max_length=100, choices = DIMENSION_CHOICES, default= '0')
	banner_cost = models.DecimalField( max_digits = 12, decimal_places = 3 )
	banner_lattitude = models.DecimalField( max_digits = 12, decimal_places = 9 )
	banner_longitude = models.DecimalField( max_digits = 12, decimal_places = 9 )
	banner_landmark = models.CharField( max_length = 200 )
	banner_status = models.CharField( max_length=100, choices = STATUS_CHOICES, default= 'available')
	banner_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


	def __str__(self):
		return '%s %s %s %s %s' % (self.banner_type, self.banner_region, self.banner_lighted,  self.banner_cost, self.banner_dimensions)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Agency(models.Model):
	agency_id = models.CharField(max_length=20, primary_key=True)
	agency_name = models.CharField(max_length=30)
	state = models.CharField(max_length=50)
	city = models.CharField(max_length=50)    


class Customer(models.Model):
	customer_name = models.CharField(max_length=50)
	customer_id = models.CharField(max_length=20, primary_key=True)
	customer_email = models.EmailField(max_length=50)
	customer_password = models.CharField(max_length=50)
	customer_contact = models.CharField(max_length=50)


