from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.contrib.auth.models import User


STATUS_CHOICES = (
	('available', 'Available'),
	('booked', 'Booked'),
)

USER_CHOICES = (
	('o', 'Owner'),
	('c', 'Customer')
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


class Category(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True)
	featured = models.BooleanField(default=None)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)


	def __unicode__(self):
		return self.title

# T-Shirt 1
# Active Wear 2
# Women's Clothing 3




class Zone(models.Model):
	zone_name = models.CharField(max_length=30)
	def __str__(self):
		return self.zone_name


class Agency(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	agency_name = models.CharField(max_length=30)
	agency_state = models.CharField(max_length=50)
	agency_city = models.CharField(max_length=50)
	zones = models.ManyToManyField(Zone,blank=True, null=True)

	def __str__(self):
		return '%s %s %s %s' % (self.id, self.agency_name, self.agency_state, self.agency_city)




class Banner(models.Model):
	def zoneList(agency):
		return agency.zones.all()
	agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone)
	banner_facing = models.CharField( max_length = 200,default= 'Facing IMS')
	banner_type = models.CharField( max_length=100, choices = TYPE_CHOICES, default= 'gantry')
	banner_lighted = models.CharField( max_length=100, choices = LIGHTED_CHOICES, default= 'n' )
	banner_dimensions = models.CharField( max_length=100, choices = DIMENSION_CHOICES, default= '0')
	banner_cost = models.DecimalField( max_digits = 12, decimal_places = 3 )
	banner_lattitude = models.DecimalField( max_digits = 12, decimal_places = 9 )
	banner_longitude = models.DecimalField( max_digits = 12, decimal_places = 9 )
	banner_landmark = models.CharField( max_length = 200 )
	banner_face_side = models.CharField( max_length = 10, choices = (('Left', 'Left'), ('Right', 'Right')) )
	banner_status = models.CharField( max_length=100, choices = STATUS_CHOICES, default= 'available')
	banner_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,default='omoads/Image/banner1.jpg')
	banner_bookingStatus = models.BooleanField(default= False)


	# banner_zone = models.CharField( max_length=100, default= 'RDC')
	

	def __str__(self):
		return '%s %s %s %s %s %s' % (self.id, self.banner_type, self.banner_landmark, self.banner_lighted,  self.banner_cost, self.banner_dimensions)


class BookingDetails(models.Model):
	banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
	bookingDate = models.DateField()
	startDate = models.DateField()
	endDate = models.DateField()
	numberDays = models.IntegerField()
	active = models.BooleanField(default = False)
	def changeBannerBookingStatus(self):
		self.banner.banner_bookingStatus = True
		self.banner.save()
	def __str__(self):
		return '%s %s' % (self.banner.id, self.bookingDate)

class PricePeriod(models.Model):
	banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()
	numberDays = models.IntegerField()
	price = models.FloatField()