from django.contrib import admin

# Register your models here.
from .models import Banner, Agency, BookingDetails,PricePeriod, Zone




admin.site.register(Banner)
admin.site.register(Agency)
admin.site.register(BookingDetails)
admin.site.register(PricePeriod)
admin.site.register(Zone)