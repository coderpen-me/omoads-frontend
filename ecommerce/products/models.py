from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.contrib.auth.models import User
import datetime

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

type_choices = {
	'gantry': 'Gantry' ,
	'unipole': 'Unipole' ,
}

LIGHTED_CHOICES = (
	('f', 'Front Lit'),
	('b', 'Back Lit'),
	('n', 'Not Lighted'),
)

light_choices = {
	'f':'Front Lit',
	'b':'Back Lit',
	'n':'Not Lighted'
	}

DIMENSION_CHOICES = (
	('0', '50x10'),
	('1', '40x10'),
	('2', '30x10'),
	('3', '20x10'),
)

Area = {
	'0':500,
	'1':400,
	'2':300,
	'3':200
}

dimension_choices = {
	'0': '50x10',
	'1': '40x10',
	'2': '30x10',
	'3': '20x10',
}


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

	def __str__(self):
		return '%s %s %s %s' % (self.id, self.agency_name, self.agency_state, self.agency_city)



def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.banner.id,ext)
    return '/'.join(['static/boardimages', filename])

class Banner(models.Model):
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
	banner_bookingStatus = models.BooleanField(default= False)
	def __str__(self):
		return '%s %s %s %s %s %s' % (self.id, self.banner_type, self.banner_landmark, self.banner_lighted,  self.banner_cost, self.banner_dimensions)
	def save(self, *args, **kwargs):
		super(Banner, self).save(*args, **kwargs) # Call the "real" save() method.
		if(self.priceperiod_set.all().count() == 0):
			startDateParsed = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").date()
			endDateParsed = datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=365)), "%Y-%m-%d").date()
			delta = endDateParsed - startDateParsed
			p = self.priceperiod_set.create(startDate=startDateParsed,endDate=endDateParsed,numberDays=delta.days,price=self.banner_cost)
			p.save()


class BannerImage(models.Model):
	def __str__(self):
		return str(self.image)

	banner = models.OneToOneField(Banner, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=content_file_name,default='boardimages/'+str(id)+'.jpg')
	

	

#maybe rename to orderDetails
class BookingDetails(models.Model):
	banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
	bookingDate = models.DateField()
	startDate = models.DateField()
	endDate = models.DateField()
	numberDays = models.IntegerField()
	active = models.BooleanField(default = False)
	def __str__(self):
		return '%s %s %s' % (self.id, self.banner.id, self.bookingDate)


class PricePeriod(models.Model):
	banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()
	numberDays = models.IntegerField()
	price = models.FloatField()

	def __str__(self):
		return '%s %s %s' % (self.startDate, self.endDate, self.price)

class Cart(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	totalPrice = models.FloatField(default = 0.0000)
	paymentAdvance = models.FloatField(default = 0.00)
	payment1 = models.FloatField(default = 0.00)
	payment2 = models.FloatField(default = 0.00)
	installationPrice = models.FloatField(default = 0.00)
	tax = models.FloatField(default = 0.00)
	totalSumPrice = models.FloatField(default = 0.00)
	def __str__(self):
		return '%s %s %s' % (self.id, self.user.username, self.totalPrice)



class CartItem(models.Model):
	banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()
	price = models.FloatField()
	dateAccept = models.BooleanField(default = True)
	def __str__(self):
		return '%s %s %s %s' % (self.id, self.startDate, self.endDate, self.price)

class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	totalPrice = models.FloatField(default = 0.0000)
	paymentAdvance = models.FloatField(default = 0.00)
	payment1 = models.FloatField(default = 0.00)
	payment2 = models.FloatField(default = 0.00)
	installationPrice = models.FloatField(default = 0.00)
	tax = models.FloatField(default = 0.00)
	totalSumPrice = models.FloatField(default = 0.00)
	status = models.IntegerField()
	def __str__(self):
		return '%s %s %s' % (self.id, self.status, self.totalSumPrice)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	bookingDetails = models.OneToOneField(BookingDetails, on_delete = models.CASCADE)
	price = models.FloatField()
	def __str__(self):
		return '%s %s %s' % (self.id,  self.price, self.bookingDetails.id)
	def delete(self, *args, **kwargs):
		super().delete(*args, **kwargs)
		if self.bookingDetails:
			self.bookingDetails.delete()


