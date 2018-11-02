from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
# Create your models here.
from django.contrib.auth.models import User
import datetime

STATUS_CHOICES = (
    ('available', 'Available'),
    ('booked', 'Booked'),
)

USER_CHOICES = (
    ('o', 'Owner'),
    ('c', 'Customer'),
)

TYPE_CHOICES = (
    ('gantry', 'Gantry'),
    ('unipole', 'Unipole'),
    ('traffic_light', 'Traffic Light Signage'),
)

type_choices = {
    'gantry': 'Gantry',
    'unipole': 'Unipole',
    'traffic_light': 'Traffic Light Signage'
}

LIGHTED_CHOICES = (
    ('f', 'Front Lit'),
    ('b', 'Back Lit'),
    ('n', 'Not Lighted'),
)

light_choices = {
    'f': 'Front Lit',
    'b': 'Back Lit',
    'n': 'Not Lighted'
}

DIMENSION_CHOICES = (
    ('0', '50x10'),
    ('1', '40x10'),
    ('2', '30x10'),
    ('3', '20x10'),
    ('4', '8x4'),
)

Area = {
    '0': 500,
    '1': 400,
    '2': 300,
    '3': 200,
    '4': 64
}

dimension_choices = {
    '0': '50x10',
    '1': '40x10',
    '2': '30x10',
    '3': '20x10',
    '4': '8x4',
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

    def __str__(self):
        return self.title


class Zone(models.Model):
    zone_name = models.CharField(max_length=30)

    def __str__(self):
        return self.zone_name


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, default="0000000000")

    def __str__(self):
        return '%s %s' % (self.user, self.phone_number)


class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=30)
    agency_state = models.CharField(max_length=50)
    agency_city = models.CharField(max_length=50)
    agency_address = models.CharField(max_length=200, default="NONE")

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.agency_name, self.agency_state, self.agency_city)

    def user_name(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def user_email(self):
        return self.user.email


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.banner.id, ext)
    return '/'.join(['static/boardimages', filename])


class Banner(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone)
    banner_facing = models.CharField(max_length=200, default='Facing IMS')
    banner_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='gantry')
    banner_lighted = models.CharField(max_length=100, choices=LIGHTED_CHOICES, default='n')
    banner_dimensions = models.CharField(max_length=100, choices=DIMENSION_CHOICES, default='0')
    banner_cost = models.DecimalField(max_digits=12, decimal_places=3)
    banner_lattitude = models.DecimalField(max_digits=12, decimal_places=9)
    banner_longitude = models.DecimalField(max_digits=12, decimal_places=9)
    banner_landmark = models.CharField(max_length=200)
    # banner_face_side = models.CharField( max_length = 10, choices = (('Left', 'Left'), ('Right', 'Right')) )
    banner_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='available')
    banner_bookingStatus = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s %s %s %s' % (
        self.id, self.banner_type, self.banner_landmark, self.banner_lighted, self.banner_cost, self.banner_dimensions)

    def save(self, *args, **kwargs):
        super(Banner, self).save(*args, **kwargs)  # Call the "real" save() method.
        if (self.priceperiod_set.all().count() == 0):
            startDateParsed = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").date()
            endDateParsed = datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=365)),
                                                       "%Y-%m-%d").date()
            delta = endDateParsed - startDateParsed
            p = self.priceperiod_set.create(startDate=startDateParsed, endDate=endDateParsed, numberDays=delta.days,
                                            price=self.banner_cost)
            p.save()

    def getSize(self):
        return str(dimension_choices[str(self.banner_dimensions)])

    def get_current_price(self):
        try:
            today_date = datetime.date.today()
            return self.priceperiod_set.filter(endDate__gte=str(today_date), startDate__lte=str(today_date))[0].price
        except Exception as e:
            return 0

    def get_banner_dimensions(self):
        return dimension_choices[self.banner_dimensions]

    def admin_edit_link(self):
        if self.id:
            change_url = reverse('admin:products_banner_change', args=(self.id,))
            return u'<a href="%s" target="_blank">Bookings</a>' % change_url
        return u''

    admin_edit_link.allow_tags = True


class BannerImage(models.Model):
    def __str__(self):
        return str(self.image)

    banner = models.OneToOneField(Banner, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=content_file_name, blank=True, null=True)
    normal_image = models.ImageField(upload_to=content_file_name, blank=True, null=True)


# maybe rename to orderDetails
class BookingDetails(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    bookingDate = models.DateField()
    startDate = models.DateField()
    endDate = models.DateField()
    numberDays = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'id : %s     banner-id: %s      banner-facing : %s     booking date : %s' % (
        self.id, self.banner.id, self.banner.banner_facing, self.bookingDate)

    def save(self, *args, **kwargs):
        bookings = self.banner.bookingdetails_set.filter(active=True)
        if self.startDate >= self.endDate:
            raise ValidationError({'date': 'invalid start end.'})
        for booking in bookings:
            if ((booking.startDate <= self.startDate and self.startDate <= booking.endDate) or
                    (booking.startDate <= self.endDate and self.endDate <= booking.endDate) or (
                            booking.startDate >= self.startDate and booking.endDate <= self.endDate)):
                if not self.pk == booking.id:
                    raise ValidationError({'date': 'already booked range.'})
        self.bookingDate = datetime.date.today()
        delta = self.endDate - self.startDate
        self.numberDays = delta.days
        super(BookingDetails, self).save(*args, **kwargs)


class PricePeriod(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    numberDays = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return 'Board ID:%s start:%s end:%s price:%s' % (self.banner.id, self.startDate, self.endDate, self.price)


class Favourite(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "banner ID:%s user:%s" % (self.banner, self.user)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totalPrice = models.FloatField(default=0.0000)
    paymentAdvance = models.FloatField(default=0.00)
    payment1 = models.FloatField(default=0.00)
    payment2 = models.FloatField(default=0.00)
    installationPrice = models.FloatField(default=0.00)
    tax = models.FloatField(default=0.00)
    totalSumPrice = models.FloatField(default=0.00)

    def __str__(self):
        return '%s %s %s' % (self.id, self.user.username, self.paymentAdvance)

    def sorted_cartitem_set(self):
        return self.cartitem_set.order_by('startDate')


class CartItem(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    price = models.FloatField()
    dateAccept = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.startDate, self.endDate, self.price)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totalPrice = models.FloatField(default=0.0000)
    paymentAdvance = models.FloatField(default=0.00)
    payment1 = models.FloatField(default=0.00)
    payment2 = models.FloatField(default=0.00)
    installationPrice = models.FloatField(default=0.00)
    tax = models.FloatField(default=0.00)
    totalSumPrice = models.FloatField(default=0.00)
    status = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.status, self.totalSumPrice, self.paymentAdvance)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    bookingDetails = models.OneToOneField(BookingDetails, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return '%s %s %s' % (self.id, self.price, self.bookingDetails.id)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if self.bookingDetails:
            self.bookingDetails.delete()


class Payments(models.Model):
    order = models.OneToOneField(Order, null=True, blank=True)
    user = models.ForeignKey(User)
    paymentId = models.CharField(max_length=150)
    paymentRequestId = models.CharField(max_length=150)
    paymentStatus = models.CharField(max_length=20)
