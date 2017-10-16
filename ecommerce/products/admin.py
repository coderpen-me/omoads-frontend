from django.contrib import admin

# Register your models here.
from .models import *


class ImageInLine(admin.StackedInline):
	model = BannerImage
class BannerAdmin(admin.ModelAdmin):
	inlines = [ImageInLine, ]

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