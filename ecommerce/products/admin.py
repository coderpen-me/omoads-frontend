from django.contrib import admin

# Register your models here.
from .models import *



class ImageInLine(admin.StackedInline):
	model = BannerImage

class PricePeriodInline(admin.TabularInline):
    model = PricePeriod
    readonly_fields = ('startDate','endDate', 'price', 'numberDays')
    can_delete = False

class BookingDetailsInline(admin.TabularInline):
    model = BookingDetails
    readonly_fields = ('startDate','endDate', 'bookingDate', 'numberDays')
    can_delete = False

class BannerAdmin(admin.ModelAdmin):
	inlines = [ImageInLine, PricePeriodInline, BookingDetailsInline, ]






admin.site.register(Banner, BannerAdmin)
admin.site.register(Agency)
admin.site.register(BookingDetails)
admin.site.register(PricePeriod)
admin.site.register(Zone)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payments)
admin.site.register(ExtendedUser)